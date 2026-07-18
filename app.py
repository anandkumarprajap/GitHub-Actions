# This code is from https://github.com/anandkumarprajap/GitHub-Actions/edit/main/app.py
# flask App
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return none
if the:
    go


@app.route('/health')
def health():
    return 'Server is up and running'
