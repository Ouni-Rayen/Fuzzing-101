from flask import Flask, send_from_directory, abort, Response
import os

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return send_from_directory(BASE_DIR, "index.html")

@app.route("/robots.txt")
def robots():
    return send_from_directory(BASE_DIR, "robots.txt")

@app.route("/colors.txt")
def colors():
    return send_from_directory(BASE_DIR, "colors.txt")

@app.route("/cyan")
def cyan():
    return send_from_directory(BASE_DIR, "cyan.html")

# Catch any other single-segment path that looks like a color
# and return a friendly 404 so fuzzing feels intentional
@app.route("/<path:color>")
def other_color(color):
    # Only respond for simple paths (no subdirs)
    if "/" in color or "." in color:
        abort(404)
    # Soft message so players know they are on the right track
    return Response(
        f"""<!DOCTYPE html>
<html><head><title>Not this shade</title>
<style>
body {{
    background: #070b1a;
    color: #8a8fa8;
    font-family: system-ui, sans-serif;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100vh;
    margin: 0;
    text-align: center;
}}
p {{ max-width: 360px; line-height: 1.6; }}
.accent {{ color: #00e5ff; }}
</style></head>
<body>
<p>This shade is not part of the official club colors.<br>
Keep exploring the <span class="accent">palette</span>.</p>
</body></html>""",
        status=404,
        mimetype="text/html"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
