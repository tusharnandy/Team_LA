
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataframe = pd.read_csv("/home/tushar/Desktop/assgn-4/Admission_Predict.csv")

'''dataframe.plot(x='GREScore', y='TOEFLScore', style='o')
plt.show()'''

x = dataframe['GREScore'].values.reshape(-1,1)
y = dataframe['TOEFLScore'].values.reshape(-1,1)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.05, random_state=0, shuffle=True)

regressor = LinearRegression()
regressor.fit(x_train, y_train) #training the algorithm

#To retrieve the intercept:
print(regressor.intercept_)
#For retrieving the slope:
print(regressor.coef_)

y_pred = regressor.predict(x_test)

df = pd.DataFrame({'Actual': y_test.flatten(), 'Predicted': y_pred.flatten()})
print(df)

plt.scatter(x_test, y_test,  color='gray')
plt.plot(x_test, y_pred, color='red', linewidth=2)
plt.show()

print('Mean Absolute Error:', metrics.mean_absolute_error(y_test, y_pred))
print('Mean Squared Error:', metrics.mean_squared_error(y_test, y_pred))
print('Root Mean Squared Error:', np.sqrt(metrics.mean_squared_error(y_test, y_pred)))
