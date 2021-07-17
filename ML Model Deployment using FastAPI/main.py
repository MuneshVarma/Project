
from datetime import datetime
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from ml_utils import load_model, predict
from typing import List
from datetime import datetime

# defining the main app
app = FastAPI(title="Loan Credit Predictor", docs_url="/")

# # calling the load_model during startup.
# # this will train the model and keep it loaded for prediction.
app.add_event_handler("startup", load_model)

# class which is expected in the payload`
class QueryIn(BaseModel):
    Status_of_existing_account: int
    Duration_of_Credit_month: int
    Payment_Status_of_Previous_Credit: int
    Purpose_of_loan: int
    Credit_Amount:int
    Value_of_Savings_accountbonds:int
    Years_of_Present_Employment:int
    Percentage_of_disposable_income:int
    Sex_Marital_Status:int
    Guarantors_Debtors:int
    Duration_in_Present_Residence:int
    Property:int
    Age_in_years:int
    Concurrent_Credits:int
    Housing:int
    No_of_Credits_at_this__Bank:int
    Occupation:int
    No_of_dependents:int
    Telephone:int
    Foreign_Worker:int

# class which is returned in the response
class QueryOut(BaseModel):
    risk_class: str
    timestamp:str


# Route definitions
@app.get("/ping")
# Healthcheck route to ensure that the API is up and running
def ping():
    return {"ping": "pong","timestamp":datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
# added get request from test case1   
@app.get("/hi")
# Healthcheck route to ensure that the API is up and running
def hi():
    return {"hi": "ML OPS-German_credit case","timestamp":datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}

@app.get("/classes")
# Healthcheck route to ensure that the API is up and running
def classes():
    return {'Status_of_existing_checking_account':{4:"no checking account",1:"<0 DM", 2: "0 <= <200 DM",3:">= 200 DM "},
        'Credit_history':{4:"critical account",3:"delay in paying off",2:"existing credits paid back duly till now",1:"all credits at this bank paid back duly",0:"no credits taken"},
        'Purpose':{0 : "car (new)", 1 : "car (used)", 2 : "furniture/equipment", 3 :"radio/television" , 4 : "domestic appliances", 5 : "repairs", 6 : "education", 7 : 'vacation',8 : 'retraining',9 : 'business',10 : 'others'},
        'Saving_account':{5 : "no savings account",1 :"<100 DM",2 : "100 <= <500 DM",3 :"500 <= < 1000 DM", 4 :">= 1000 DM"},
        'Present_employment':{5:">=7 years", 4:"4<= <7 years",  3:"1<= < 4 years", 2:"<1 years",1:"unemployed"},
        'Personal_status_and_sex':{ 5:"female:single",4:"male:married/widowed",3:"male:single", 2:"female:divorced/separated/married", 1:"male:divorced/separated"},
        'Other_debtors_guarantors':{1:"none", 2:"co-applicant", 3:"guarantor"},
        'Property':{1:"real estate", 2:"savings agreement/life insurance", 3:"car or other", 4:"unknown / no property"},
        'Other_installment_plans':{3:"none", 2:"store", 1:"bank"},
        'Housing':{3:"for free", 2:"own", 1:"rent"},
        'Job':{4:"management/ highly qualified employee", 3:"skilled employee / official", 2:"unskilled - resident", 1:"unemployed/ unskilled  - non-resident"},
        'Telephone':{2:"yes", 1:"none"},
        'foreign_worker':{1:"yes", 2:"no"},
        'risk':{1:"Good Risk", 0:"Bad Risk"},
            }

# added get request from test case2
# @app.get("/hello")
# # Healthcheck route to ensure that the API is up and running
# def hello():
#     return {"hello": "ML OPS-iris-test case2","timestamp":datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}

@app.post("/predict_class", response_model=QueryOut, status_code=200)
# Route to do the prediction using the ML model defined.
# Payload: QueryIn containing the parameters
# Response: QueryOut containing the flower_class predicted (200)
def predict_class(query_data: QueryIn):
    output = {"risk_class": predict(query_data),"timestamp":datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    return output

# @app.post("/feedback_loop", status_code=200)
# # Route to further train the model based on user input in form of feedback loop
# # Payload: FeedbackIn containing the parameters and correct flower class
# # Response: Dict with detail confirming success (200)
# def feedback_loop(data: List[FeedbackIn]):
#     retrain(data)
#     return {"detail": "Feedback loop successful"}

# Main function to start the app when main.py is called
if __name__ == "__main__":
    # Uvicorn is used to run the server and listen for incoming API requests on 0.0.0.0:8888
    uvicorn.run("main:app", host="127.0.0.1", port=8888, reload=True)
