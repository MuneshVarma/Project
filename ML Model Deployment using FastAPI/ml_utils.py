from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import pickle

# define a Gaussain NB classifier
# clf = GaussianNB()
# clf1= DecisionTreeClassifier(random_state=0,max_depth=5)

# define the class encodings and reverse encodings
classes = {0: "Bad risk", 1: "Good Risk"}
r_classes = {y: x for x, y in classes.items()}

# function to train and load the model during startup
def load_model():
    # load the dataset from the official sklearn datasets
    with open('best_model','rb') as f:
         model=pickle.load(f)

# function to predict the flower using the model
def predict(query_data):
    x = list(query_data.dict().values())
    with open('best_model','rb') as f:
         model=pickle.load(f)
    prediction = model.predict([x])[0]
    print(f"Model prediction: {classes[prediction]}")
    return(classes[prediction])
