import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Home"

@app.route("/ping")
def ping_host():
    ip_address = request.args.get('ip')

    if ip_address:
       subprocess.run(
            "ping -c 1 " + ip_address,
            shell=True
        )
       return "Done!"

    return ""


if "__main__" in __name__:
    app.run(host='0.0.0.0')
