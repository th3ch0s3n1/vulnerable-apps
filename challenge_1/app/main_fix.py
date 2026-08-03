import re
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Home"

@app.route("/ping")
def ping_host():
    ip_address = request.args.get('ip')

    if not ip_address:
        return "Nebyla zadána doména nebo IP adresa", 400

    DOMAIN_OR_IP_REGEX = r"^[a-zA-Z0-9.-]+$"

    if not re.match(DOMAIN_OR_IP_REGEX, ip_address):
        return "Neplatná doména nebo IP adresa", 400

    try:

        result = subprocess.run(
            ["ping", "-c", "1", str(ip_address)],
            capture_output=True,
            text=True,
            timeout=5
        )

        return f"{result.stdout}"

    except subprocess.TimeoutExpired:
        return "Ping vypršel (timeout)", 504


if "__main__" in __name__:
    app.run(host='0.0.0.0')
