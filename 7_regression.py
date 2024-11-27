import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# Step-1: load the dataset
dataset = pd.read_csv('Sal_Data.csv')
dataset.head()
# Step-2: data preprocessing
X = dataset.iloc[:, :-1].values # extract independent variable array
y = dataset.iloc[:,1].values # extract dependent variable vector
print(X)
print(y)
# Step-3: splitting the dataset into training and testing dataset
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=1/3,random_state=0)
print("Training set:",X_train,"\n",y_train)
print("Testing set:",X_test,"\n",y_test)
# Step-4: fitting the regression model
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,y_train) #actually produces the linear eqn for the data
# Step-5: predicting the test set results
y_pred = regressor.predict(X_test)
print("predicted salaries are:",y_pred)
print("actual salaries are:",y_test)
# Step-6: visualizing the results
#plot for the TRAIN
plt.scatter(X_train, y_train, color='red') # plotting the observation line
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
plt.title("Salary vs Experience (Training set)") # stating the title of the graph
plt.xlabel("Years of experience") # adding the name of x-axis
plt.ylabel("Salaries") # adding the name of y-axis
plt.show() # specifies end of graph
#plot for the TEST
plt.scatter(X_test, y_test, color='red')
plt.plot(X_train, regressor.predict(X_train), color='blue') # plotting the regression line
plt.title("Salary vs Experience (Testing set)")
plt.xlabel("Years of experience")
plt.ylabel("Salaries")
plt.show()
