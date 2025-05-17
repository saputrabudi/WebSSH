# WebSSH - Web Tabanlı SSH Terminali

Tarayıcı üzerinden SSH bağlantılarına izin veren web tabanlı bir SSH terminal uygulaması.

## Uygulama Hakkında

WebSSH, kullanıcıların doğrudan tarayıcıdan SSH bağlantıları yapmasına olanak tanıyan Python (Flask ve Socket.IO) ile oluşturulmuş bir uygulamadır. Bu uygulama şunları kullanır:

- **Backend**: Gerçek zamanlı iletişim için Flask (Python) ve Socket.IO
- **Frontend**: Terminal emülatörü olarak Xterm.js ile HTML, CSS ve JavaScript
- **SSH Bağlantısı**: SSH bağlantılarını yönetmek için Paramiko (Python kütüphanesi)

## Temel Özellikler

- Duyarlı web terminal arayüzü
- Tarayıcıdan doğrudan SSH bağlantıları
- Etkileşimli terminal deneyimi
- Minimalist ve modern tasarım

## Uygulama Yapısı

- `app.py`: SSH bağlantılarını ve Socket.IO iletişimini yöneten ana Flask uygulama dosyası
- `templates/terminal.html`: Etkileşimli terminalli ana web sayfası
- `static/css/style.css`: Terminal arayüzü için stil dosyası
- `__pycache__/`: Python önbellek dosyaları

## Kullanım

1. `python app.py` komutu ile Flask uygulamasını çalıştırın
2. Tarayıcı üzerinden `http://localhost:5000` adresinden uygulamaya erişin
3. SSH bağlantı detaylarını girin (sunucu, kullanıcı adı, şifre)
4. Terminal oturumu başlatmak için Connect düğmesine tıklayın

## Kullanılan Teknolojiler

- Flask: Python web çerçevesi
- Socket.IO: Sunucu ve tarayıcı arasında gerçek zamanlı iletişim için
- Paramiko: Python için SSH kütüphanesi
- Xterm.js: JavaScript terminal emülatörü
- HTML/CSS/JavaScript: Kullanıcı arayüzü

## Kurulum

```bash
# Depoyu klonlayın
git clone https://github.com/saputrabudi/WebSSH.git

# Dizine girin
cd WebSSH

# Bağımlılıkları yükleyin
pip install flask flask-socketio paramiko

# Uygulamayı çalıştırın
python app.py
```

Tarayıcınızdan `http://localhost:5000` adresinden uygulamaya erişin

## Saputra Budi tarafından geliştirilmiştir 