import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def takeInput():
    featuresAndData = {}
    n = int(input("Enter the number of features you want to input: "))

    for i in range(n):
        name = input("Enter the feature name: ")
        featuresAndData[name] = np.array(eval(input("Enter the data of this feature(comma separated): ")))

    target = input("Enter the dependent value(key): ")
    
    keys = list(featuresAndData.keys())
    for i in range(n-1):
        if len(featuresAndData[keys[i]]) != len(featuresAndData[keys[i+1]]):
            return "the dataset is not processed", None
    
    if target not in featuresAndData:
        return "The target value is not there", None
        
    return featuresAndData, target


def dataFrame():
    inputDataSet, target = takeInput()
    if type(inputDataSet) == str:
        raise Exception(inputDataSet)
        
    df = pd.DataFrame(inputDataSet)
    
    X = df.drop(columns=[target])
    y = df[target]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = linear_model.LinearRegression()
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    print("Coefficients:", model.coef_)
    print("Intercept:", model.intercept_)
    
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.title("Actual vs Predicted")
    plt.show()

dataFrame()