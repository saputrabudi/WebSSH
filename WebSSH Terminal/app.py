from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit
import paramiko
import threading
import time
from threading import Lock

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
thread_lock = Lock()
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='threading')
ssh_clients = {}

@app.route('/')
def index():
    return render_template('terminal.html')

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in ssh_clients:
        with thread_lock:
            if request.sid in ssh_clients:
                ssh_clients[request.sid]['client'].close()
                del ssh_clients[request.sid]
    print('Client disconnected')

@socketio.on('ssh_connect')
def handle_ssh_connect(data):
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(
            data['host'],
            username=data['username'],
            password=data['password']
        )
        
        channel = client.invoke_shell()
        channel.setblocking(0)
        
        with thread_lock:
            ssh_clients[request.sid] = {
                'client': client,
                'channel': channel,
                'thread_running': True
            }
        
        def read_output(sid):
            app_context = app.app_context()
            app_context.push()
            
            while True:
                with thread_lock:
                    if sid not in ssh_clients or not ssh_clients[sid]['thread_running']:
                        break
                    try:
                        channel = ssh_clients[sid]['channel']
                        if channel.recv_ready():
                            output = channel.recv(1024).decode('utf-8', errors='ignore')
                            socketio.emit('ssh_output', {'output': output}, room=sid)
                    except Exception as e:
                        print(f"Error reading from channel: {e}")
                        break
                time.sleep(0.1)
            
            app_context.pop()
        
        thread = threading.Thread(target=read_output, args=(request.sid,))
        thread.daemon = True
        thread.start()
        
        emit('ssh_connected')
    except Exception as e:
        emit('ssh_error', {'error': str(e)})

@socketio.on('ssh_input')
def handle_ssh_input(data):
    with thread_lock:
        if request.sid in ssh_clients:
            try:
                channel = ssh_clients[request.sid]['channel']
                channel.send(data['input'])
            except Exception as e:
                emit('ssh_error', {'error': str(e)})

@socketio.on_error_default
def default_error_handler(e):
    print(f"SocketIO error: {str(e)}")
    emit('ssh_error', {'error': str(e)})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)