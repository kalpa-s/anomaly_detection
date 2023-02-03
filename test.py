import pandas as pd
import pickle
import numpy as np

model = open(
    'C:/Users/Kalpagam/udemy_bootcamp/ml_projects/anomaly_detection/trained_model.pkl', 'rb')
trained_model = pickle.load(model)

x_test = input("Enter a current reading ")

x_test = np.asarray(x_test).reshape(-1, 1)

result = trained_model.predict(x_test)

if (result == [1]):
    print("Anomaly")
else:
    print("No Anomaly")
