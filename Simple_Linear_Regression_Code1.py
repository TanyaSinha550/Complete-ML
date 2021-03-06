#Importing The Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Importing the dataset
dataset=pd.read_csv('Salary_Data.csv')
X=dataset.iloc[:,:-1].values
y=dataset.iloc[:,-1].values

#No missing data and no categorical values

# Splitting the dataset into training and test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)

#No need of feature scaling as linear Regression model itself does Feature Scaling

#Fitting the Simple Linear Regression Model to the training set
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,y_train)

# Predicting the Test Set results
y_pred=regressor.predict(X_test)

# Visualizing the train set results
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,regressor.predict(X_train),color='blue')
plt.title("Experience vs Salary (training Set)")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Visualizing the test set results
plt.scatter(X_test,y_test,color='red')
plt.plot(X_test,y_pred,color='blue')
plt.title("Experience vs Salary (test Set)")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()