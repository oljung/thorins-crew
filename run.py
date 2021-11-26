"""
Runs the flask application and renders templates
"""
import os
import json
from flask import Flask, render_template, request, flash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")


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
    data = []
    with open("data/company.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("about.html", page_title="About", company=data)


@app.route('/about/<member_name>')
def about_member(member_name):
    """
    Rendera about pages for different members
    """
    member = {}
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["url"] == member_name:
                member = obj
    return render_template("member.html", member=member)


@app.route('/contact', methods=["GET", "POST"])
def contact():
    """
    Renders contact page
    """
    if request.method == "POST":
        flash(f'Thansk {request.form.get("name")} message recieved')
    return render_template("contact.html", page_title="Contact")


@app.route("/careers")
def careers():
    """
    Renders careers page
    """
    return render_template("careers.html", page_title="Careers")


if __name__ == "__main__":
    app.run(
        host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', '5000')),
        debug=True
    )
