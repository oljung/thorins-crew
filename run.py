"""
Runs the flask application and renders templates
"""
import os
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """
    Renders the index.html file
    """
    return render_template("index.html")


@app.route('/about')
def about():
    """
    Render the about.html file
    """
    return render_template("about.html")


@app.route('/contact')
def contact():
    """
    Renders contact page
    """
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True
    )
