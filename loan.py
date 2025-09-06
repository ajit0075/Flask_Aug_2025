from flask import Flask , request , jsonify
import pickle

app= Flask(__name__)

with open('classifier.pkl', 'rb') as f :
    model= pickle.load(f)


 
@app.route("/", methods =['GET'])
def hell():
    return "<h1> Loan app Application </h1>"

@app.route("/predict", methods= ['GET'])
def pred():
    return "<h1> I will make pridict</h1>"

@app.route("/predict" , methods =['POST'])
def predict_post():
    loan_req= request.get_json()
    print(loan_req)
    
    if  loan_req["Gender"]=="Male":
        Gender = 0
    else:
        Gender =0
    
    if loan_req["Married"] =="No":
        Married = 0
    else:
        Married=1

    ApplicationIncome = loan_req["ApplicationIncome"]  
    LoanAmount = loan_req["LoanAmount"]  
    credict_histroy = loan_req["credicHistory"]

    input_data = [Gender,Married,ApplicationIncome,LoanAmount,credict_histroy ]
    print(input_data)
    result= model.predict([input_data])

    if  result[0]== 1 :
        pred= "Approved "
    else:
        pred = "Rejected"
    
    return jsonify({"Loan approval status is ":pred})
    
    
    #return jsonify({'prediction': result.tolist()}) if we dont use if else of predict