from flask import Flask, request, jsonify, render_template_string
import requests
import threading

app = Flask(__name__)

connected_clients = set()  # نگه داشتن آی‌پی کلاینت‌ها

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Server Dashboard</title>
</head>
<body>
    <h2>Connected Clients</h2>
    <ul>
    {% for ip in clients %}
        <li>{{ ip }}</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route('/')
def dashboard():
    return render_template_string(HTML_TEMPLATE, clients=connected_clients)

@app.route('/proxy', methods=['GET'])
def proxy():
    client_ip = request.remote_addr
    connected_clients.add(client_ip)
    
    url = request.args.get('url')
    if not url:
        return "Missing 'url' parameter", 400
    
    if not url.startswith('http'):
        url = 'http://' + url
    
    try:
        resp = requests.get(url, timeout=10)
        headers = [(k, v) for k, v in resp.headers.items() if k.lower() not in ["content-encoding", "transfer-encoding", "connection"]]
        return (resp.content, resp.status_code, headers)
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)
