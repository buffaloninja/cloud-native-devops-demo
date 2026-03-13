# Import Flask web Framework
from flask import Flask
# import Prometheus monitoring tools
from prometheus_client import Counter, generate_latest

# Create the Flask web application
app = Flask(__name__)

# Countermetric to track total number of request
REQUEST_COUNT = Counter('request_count', 'Total Request Count')

# Home route for the application
@app.route("/")
def home():
    # Increment request counter each time page is visited
    REQUEST_COUNT.inc()
    return "Hello from my DevOps portfolio project!"

# Health check endpoint used for monitoring systems
@app.route("/health")
def health():
    return "OK"
# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return generate_latest()

# Run the Flask application
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)