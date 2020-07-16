from flask import current_app as app
from flask import render_template

@app.route("/")
def home():
    """Serve homepage template."""
    return render_template(
        'index.html'
    )
@app.route("/haha")
def home1():
    """Serve homepage template."""
    print ("dada")
    return render_template(
        'index.html'
    )