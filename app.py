from flask import Flask
from flask import request
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hola como estas :D"

 @app.route("/index")
def index():
    return open("index.html").read()

@app.route("/suma")
def suma():
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    restun n1 + n2
    
    @app.route("/resta")
def resta():
    n1 = request.args.get('n1')
    n2 = request.args.get('n2')
    restun str(int(n1) - int(n2))
   
@app.route("/index")
def index():
    return open("index.html").read()
 
 if __name__ == "__main__":
    app.run()
