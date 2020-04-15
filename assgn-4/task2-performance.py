import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataframe = pd.read_csv("/home/tushar/Admission_Predict.csv")

'''dataframe.plot(x='GREScore', y='TOEFLScore', style='o')
plt.show()'''

x = dataframe['GREScore'].values.reshape(-1,1)
y = dataframe['TOEFLScore'].values.reshape(-1,1)

regressor = LinearRegression()
regressor.fit(x, y) #training the algorithm

#To retrieve the intercept:
c = regressor.intercept_
#For retrieving the slope:
m = regressor.coef_

'''gre = input("Enter GRE Score: ")
gre = float(gre)
toefl = gre*regressor.coef_ + regressor.intercept_
print(f"predicted TOEFL score: {toefl}")'''


y_test = np.array([290, 322, 296, 291, 320, 298, 333, 310, 300, 328, 301, 314, 327, 325, 316, 331, 339, 317, 318, 324])

y_pred = y_test*m + c

df = pd.DataFrame({'Input': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)
