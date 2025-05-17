# WebSSH - Webbasiertes SSH-Terminal

Eine webbasierte SSH-Terminal-Anwendung, die SSH-Verbindungen über einen Browser ermöglicht.

## Über die Anwendung

WebSSH ist eine mit Python (Flask und Socket.IO) entwickelte Anwendung, die es Benutzern ermöglicht, SSH-Verbindungen direkt vom Browser aus herzustellen. Diese Anwendung verwendet:

- **Backend**: Flask (Python) mit Socket.IO für Echtzeit-Kommunikation
- **Frontend**: HTML, CSS und JavaScript mit Xterm.js als Terminal-Emulator
- **SSH-Verbindung**: Paramiko (Python-Bibliothek) zur Verwaltung von SSH-Verbindungen

## Hauptfunktionen

- Responsive Web-Terminal-Oberfläche
- Direkte SSH-Verbindungen vom Browser aus
- Interaktive Terminal-Erfahrung
- Minimalistisches und modernes Design

## Anwendungsstruktur

- `app.py`: Haupt-Flask-Anwendungsdatei, die SSH-Verbindungen und Socket.IO-Kommunikation verwaltet
- `templates/terminal.html`: Haupt-Webseite mit interaktivem Terminal
- `static/css/style.css`: Styling für die Terminal-Oberfläche
- `__pycache__/`: Python-Cache-Dateien

## Verwendung

1. Starten Sie die Flask-Anwendung mit dem Befehl `python app.py`
2. Greifen Sie über den Browser unter `http://localhost:5000` auf die Anwendung zu
3. Geben Sie die SSH-Verbindungsdetails ein (Host, Benutzername, Passwort)
4. Klicken Sie auf die Connect-Schaltfläche, um eine Terminal-Sitzung zu starten

## Verwendete Technologien

- Flask: Python-Web-Framework
- Socket.IO: Für Echtzeit-Kommunikation zwischen Server und Browser
- Paramiko: SSH-Bibliothek für Python
- Xterm.js: JavaScript-Terminal-Emulator
- HTML/CSS/JavaScript: Benutzeroberfläche

## Installation

```bash
# Repository klonen
git clone https://github.com/saputrabudi/WebSSH.git

# In das Verzeichnis wechseln
cd WebSSH

# Abhängigkeiten installieren
pip install flask flask-socketio paramiko

# Anwendung starten
python app.py
```

Greifen Sie über Ihren Browser unter `http://localhost:5000` auf die Anwendung zu

## Von Saputra Budi 