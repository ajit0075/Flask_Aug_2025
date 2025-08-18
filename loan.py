from flask import Flask

app= Flask(__name__)

@app.route("/", methods =['GET'])
def hell():
    return "<h1> Loan app Application </h1>"

@app.route("/predict", methods= ['GET'])
def pred():
    return "<h1> I will make pridict</h1>"

