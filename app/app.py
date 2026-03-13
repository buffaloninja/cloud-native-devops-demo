from flask import Flask
from prometheus_client import Counter, generate_latest

app = Flask(__name__)

REQUEST_COUNT = Counter('request_count', 'Total Request Count')

@app.route("/")
def home():
    REQUEST_COUNT.inc()
    return "Hello from my DevOps portfolio project!"

@app.route("/health")
def health():
    return "OK"

@app.route("/metrics")
def metrics():
    return generate_latest()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)