from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.after_request
def add_security_headers(response):
    csp = [
        "default-src 'self'",
        "script-src 'self' https://cdn.jsdelivr.net",
        "style-src 'self' https://cdn.jsdelivr.net 'unsafe-inline'",
        "frame-ancestors 'none'; base-uri 'self'"
    ]
    response.headers['Content-Security-Policy'] = "; ".join(csp)
    response.headers['X-Content-Type-Options'] = 'nosniff'
    return response

TEMPLATE = """
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.css">
<div style="padding: 2rem;"><h1>Výsledky: {{ query }}</h1></div>
"""

@app.route("/")
def index():
    user_input = request.args.get("q", "Hledat...")
    
    return render_template_string(TEMPLATE, query=user_input)

if __name__ == "__main__":
    app.run()
