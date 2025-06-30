
from flask import Flask, jsonify, request
import threading
import time

app = Flask(__name__)

@app.route('/')
def health_check():
    return jsonify({
        "status": "active",
        "service": "Telegram Bot API",
        "timestamp": time.time()
    })

@app.route('/status')
def bot_status():
    return jsonify({
        "bot_status": "running",
        "message": "Telegram bot is active"
    })

@app.route('/webhook', methods=['POST'])
def webhook():
    # Здесь можно обрабатывать внешние запросы
    data = request.get_json()
    return jsonify({"received": True, "data": data})

def run_flask():
    app.run(host='0.0.0.0', port=8080, debug=False)

if __name__ == '__main__':
    run_flask()
