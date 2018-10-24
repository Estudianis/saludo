from flask import Flask
from flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hola como estas :D"
 
@app.route("/index")
def index():
    return open("index.html").read()
