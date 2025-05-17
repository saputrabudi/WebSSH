# WebSSH - Terminal SSH Berbasis Web

Aplikasi terminal SSH berbasis web yang memungkinkan koneksi SSH melalui browser.

## Tentang Aplikasi

WebSSH adalah aplikasi yang dibangun dengan Python (Flask dan Socket.IO) yang memungkinkan pengguna untuk melakukan koneksi SSH langsung dari browser. Aplikasi ini menggunakan:

- **Backend**: Flask (Python) dengan Socket.IO untuk komunikasi realtime
- **Frontend**: HTML, CSS, dan JavaScript dengan Xterm.js sebagai emulator terminal
- **Koneksi SSH**: Paramiko (library Python) untuk mengelola koneksi SSH

## Fitur Utama

- Antarmuka terminal web yang responsif
- Koneksi SSH langsung dari browser
- Pengalaman terminal yang interaktif
- Desain minimalis dan modern

## Struktur Aplikasi

- `app.py`: File utama aplikasi Flask yang menangani koneksi SSH dan komunikasi Socket.IO
- `templates/terminal.html`: Halaman web utama dengan terminal interaktif
- `static/css/style.css`: Styling untuk antarmuka terminal
- `__pycache__/`: File cache Python

## Cara Penggunaan

1. Jalankan aplikasi Flask dengan perintah `python app.py`
2. Akses aplikasi melalui browser di `http://localhost:5000`
3. Masukkan detail koneksi SSH (host, username, password)
4. Klik tombol Connect untuk memulai sesi terminal

## Teknologi yang Digunakan

- Flask: Web framework Python
- Socket.IO: Untuk komunikasi realtime antara server dan browser
- Paramiko: Library SSH untuk Python
- Xterm.js: Emulator terminal JavaScript
- HTML/CSS/JavaScript: Antarmuka pengguna

## Instalasi

```bash
# Clone repository
git clone [url-repository]

# Masuk ke direktori
cd WebSSH

# Instal dependensi
pip install flask flask-socketio paramiko

# Jalankan aplikasi
python app.py
```

Akses aplikasi di browser melalui `http://localhost:5000`

## By Saputra Budi 