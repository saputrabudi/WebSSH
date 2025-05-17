# WebSSH - Web-Based SSH Terminal

A web-based SSH terminal application that allows SSH connections through a browser.

## About the Application

WebSSH is an application built with Python (Flask and Socket.IO) that allows users to make SSH connections directly from the browser. This application uses:

- **Backend**: Flask (Python) with Socket.IO for real-time communication
- **Frontend**: HTML, CSS, and JavaScript with Xterm.js as the terminal emulator
- **SSH Connection**: Paramiko (Python library) to manage SSH connections

## Key Features

- Responsive web terminal interface
- Direct SSH connections from the browser
- Interactive terminal experience
- Minimalist and modern design

## Application Structure

- `app.py`: Main Flask application file that handles SSH connections and Socket.IO communication
- `templates/terminal.html`: Main web page with interactive terminal
- `static/css/style.css`: Styling for the terminal interface
- `__pycache__/`: Python cache files

## How to Use

1. Run the Flask application with the command `python app.py`
2. Access the application via browser at `http://localhost:5000`
3. Enter SSH connection details (host, username, password)
4. Click the Connect button to start a terminal session

## Technologies Used

- Flask: Python web framework
- Socket.IO: For real-time communication between server and browser
- Paramiko: SSH library for Python
- Xterm.js: JavaScript terminal emulator
- HTML/CSS/JavaScript: User interface

## Installation

```bash
# Clone repository
git clone https://github.com/saputrabudi/WebSSH.git

# Enter directory
cd WebSSH

# Install dependencies
pip install flask flask-socketio paramiko

# Run the application
python app.py
```

Access the application in your browser via `http://localhost:5000`

## By Saputra Budi 