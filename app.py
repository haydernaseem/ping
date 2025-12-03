from flask import Flask
import threading
import time
import requests

app = Flask(__name__)

SERVERS = [
    "https://oilnova-chat-backend-1.onrender.com",
    "https://polyy-plotting.onrender.com",
    "https://ai-lift.onrender.com",
    "https://oilnova-dca.onrender.com",
    "https://petroai-knn.onrender.com"
]

def cycle_ping():
    while True:
        print("🔵 2-minute ping cycle started...")
        start = time.time()

        # 2 minutes active ping
        while time.time() - start < 120:
            for url in SERVERS:
                try:
                    requests.get(url, timeout=10)
                    print("Ping →", url)
                except Exception as e:
                    print("Failed →", url, e)
            time.sleep(10)

        print("🟡 Sleeping 3 minutes...")
        time.sleep(180)


# Start loop automatically at server launch
threading.Thread(target=cycle_ping, daemon=True).start()


@app.route("/")
def home():
    return "Ping cycle is running automatically."


@app.route("/start")
def start():
    return "Already running automatically. No need to start manually."
