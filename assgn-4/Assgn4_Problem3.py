import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics



df = pd.read_csv("Admission_Predict_LA.csv")
df.drop(columns=['Serial No.'], inplace=True)
headers = list(df.columns)
target = headers.pop()
X = df[headers].values
y = df[target].values



plt.figure(figsize=(15,10))
plt.tight_layout()
seabornInstance.distplot(df[target])



X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



regressor = LinearRegression()
regressor.fit(X_train, y_train)



coeff_df = pd.DataFrame(regressor.coef_, headers, columns=['Coefficient'])
print(coeff_df)



y_pred = regressor.predict(X_test)



final = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print(final.head(25))



show = final.head(25)
show.plot(kind='bar',figsize=(16,10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()



MAE = metrics.mean_absolute_error(y_test, y_pred)
RMSE = np.sqrt(metrics.mean_squared_error(y_test, y_pred))
print(f"Mean Absolute Error: {MAE}")
print(f"Root Mean Squared Error: {RMSE}")
print(np.mean(y))
print(f"Error % is {RMSE/(np.mean(y)) * 100}")
