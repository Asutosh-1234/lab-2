import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

def takeInput():
    featuresAndData = {}
    n = int(input("Enter the number of features you want to input: "))

    for i in range(n):
        name = (input("Enter the feature name: "))
        featuresAndData[name] = np.array(eval(input("Enter the data of this feature(comma separated): ")))

    target = input("Enter the dependent value(key): ")
    for i in range(n-1):
        
        if len(featuresAndData[i]) != len(featuresAndData[i+1]):
            return "the dataset is not processed"
    
    if target not in featuresAndData:
        return "The target value is not there"
        
    return featuresAndData


def dataFrame():
    inputDataSet = takeInput()
    if type(inputDataSet) == str:
        raise Exception(inputDataSet)
    x = pd.DataFrame(inputDataSet)
    
    

dataFrame()