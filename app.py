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

running = False

def cycle_ping():
    global running
    if running:
        return
    running = True

    while True:
        # Ping for 1 minute
        print("🔵 Starting 1-minute ping...")
        start = time.time()
        while time.time() - start < 60:
            for url in SERVERS:
                try:
                    requests.get(url, timeout=10)
                    print("Ping →", url)
                except:
                    print("Failed →", url)
            time.sleep(10)

        # Sleep 3 minutes
        print("🟡 Sleeping for 3 minutes...")
        time.sleep(180)


@app.route("/start")
def start():
    t = threading.Thread(target=cycle_ping)
    t.daemon = True
    t.start()
    return "Ping cycle started."


@app.route("/")
def home():
    return "Ping cycle server is active."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
