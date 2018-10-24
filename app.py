from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hola como estas :D"

if__name__ == "__main__":
   app.run()

@app.route("/index")
def index():
    return open("index.html").read()
 

