# WebSSH - 基于网页的SSH终端

一个基于网页的SSH终端应用程序，允许通过浏览器进行SSH连接。

## 关于应用

WebSSH是一个使用Python（Flask和Socket.IO）构建的应用程序，允许用户直接从浏览器进行SSH连接。该应用程序使用：

- **后端**：Flask（Python）和Socket.IO用于实时通信
- **前端**：HTML，CSS和JavaScript，使用Xterm.js作为终端模拟器
- **SSH连接**：Paramiko（Python库）用于管理SSH连接

## 主要功能

- 响应式网页终端界面
- 直接从浏览器进行SSH连接
- 交互式终端体验
- 简约现代的设计

## 应用结构

- `app.py`：主要Flask应用文件，处理SSH连接和Socket.IO通信
- `templates/terminal.html`：带有交互式终端的主网页
- `static/css/style.css`：终端界面的样式设计
- `__pycache__/`：Python缓存文件

## 使用方法

1. 使用命令`python app.py`运行Flask应用程序
2. 通过浏览器访问`http://localhost:5000`
3. 输入SSH连接详情（主机，用户名，密码）
4. 点击Connect按钮开始终端会话

## 使用的技术

- Flask：Python网页框架
- Socket.IO：用于服务器和浏览器之间的实时通信
- Paramiko：Python的SSH库
- Xterm.js：JavaScript终端模拟器
- HTML/CSS/JavaScript：用户界面

## 安装

```bash
# 克隆仓库
git clone https://github.com/saputrabudi/WebSSH.git

# 进入目录
cd WebSSH

# 安装依赖
pip install flask flask-socketio paramiko

# 运行应用程序
python app.py
```

通过浏览器访问`http://localhost:5000`使用应用程序

## 作者：Saputra Budi 