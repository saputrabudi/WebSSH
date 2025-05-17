# WebSSH - ウェブベースのSSHターミナル

ブラウザを通じてSSH接続を可能にするウェブベースのSSHターミナルアプリケーション。

## アプリケーションについて

WebSSHは、ユーザーがブラウザから直接SSH接続を行うことができるPython（FlaskとSocket.IO）で構築されたアプリケーションです。このアプリケーションは以下を使用しています：

- **バックエンド**：リアルタイム通信のためのFlask（Python）とSocket.IO
- **フロントエンド**：ターミナルエミュレータとしてXterm.jsを使用したHTML、CSS、およびJavaScript
- **SSH接続**：SSH接続を管理するためのParamiko（Pythonライブラリ）

## 主な機能

- レスポンシブなウェブターミナルインターフェース
- ブラウザからの直接SSH接続
- インタラクティブなターミナル体験
- ミニマリストでモダンなデザイン

## アプリケーション構造

- `app.py`：SSH接続とSocket.IO通信を処理するメインFlaskアプリケーションファイル
- `templates/terminal.html`：インタラクティブなターミナルを持つメインウェブページ
- `static/css/style.css`：ターミナルインターフェースのスタイリング
- `__pycache__/`：Pythonキャッシュファイル

## 使用方法

1. `python app.py`コマンドでFlaskアプリケーションを実行する
2. ブラウザから`http://localhost:5000`でアプリケーションにアクセスする
3. SSH接続詳細（ホスト、ユーザー名、パスワード）を入力する
4. Connectボタンをクリックしてターミナルセッションを開始する

## 使用技術

- Flask：Pythonウェブフレームワーク
- Socket.IO：サーバーとブラウザ間のリアルタイム通信のため
- Paramiko：PythonのSSHライブラリ
- Xterm.js：JavaScriptターミナルエミュレータ
- HTML/CSS/JavaScript：ユーザーインターフェース

## インストール

```bash
# リポジトリをクローン
git clone https://github.com/saputrabudi/WebSSH.git

# ディレクトリに移動
cd WebSSH

# 依存関係をインストール
pip install flask flask-socketio paramiko

# アプリケーションを実行
python app.py
```

ブラウザから`http://localhost:5000`でアプリケーションにアクセスしてください

## 作者：Saputra Budi 