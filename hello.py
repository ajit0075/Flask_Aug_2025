from flask import Flask

# main variable 
app = Flask(__name__)

@app.route("/")
def hello():
  return "hello there my first web page!!"

@app.route("/ping", method =['GET'])
def anything():
  return "message why pinging me"

@app.route("/ping")
def anything():
  return "message why pinging me"
