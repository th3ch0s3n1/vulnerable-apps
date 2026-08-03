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

@app.route("/")
def index():
    user_input = request.args.get("q", "Hledat...")
    s = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.css"
    template = f"""
    <link rel="stylesheet" href="{s}">
    <div style="padding: 2rem;"><h1>Výsledky: {user_input}</h1></div>
    """
    return render_template_string(template)

if __name__ == "__main__":
    app.run()
