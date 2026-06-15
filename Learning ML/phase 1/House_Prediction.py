import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

df  = pd.read_csv('house.csv')

print(df)

data = df.head()
# print(data)
# print(df.info())
# print(df.describe())
# print(df.isnull().sum())

# feature and target selection 

X = df[['area', 'bedrooms', 'age']]
y = df['price']


# train test split
X_train,  X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state= 42)

# Model Training 

model = LinearRegression()

model.fit(X_train, y_train)


pred = model.predict(X_test)
print(pred)

# print : 
  # Actual Price
  # Predicted Price


comparison = pd.DataFrame({
  "Actual" : y_test.values,
  "predicted" : pred
})

print(comparison)

# print(f"Actual Pice : {y_test} Predicted Price : {pred}")

# Evaluation
# Mean Squared Error :  MSE is the average squared distance actual values and predicted values - on average, it tells how far off our model's prediction is 
# heavily penalize the error if it is massive - MSE = i/n SUmmation of (y_act - y_pred)^2


# The R^2 score is a standardized metric. It measures the proportion of variance in the dependent variable that is predictable from the independent variables.

# R^2 = 1 - SS_res / SS_tot 

mse = mean_squared_error(y_test, pred)
r2 = r2_score(y_test, pred)

print(f"MSE : {mse}")
print(f"R2 Score : {r2}") 
# output : R^2 Score : 0.9972868526431378
# R^2 = 1: Perfect model. It explains 100% of the variance.
# R^2 = 0: Your model is just as lazy/accurate as guessing the average line.
# R^2 < 0: Your model is actively worse than just guessing the average line.


# Model Interpretation
print(model.coef_)
print(model.intercept_)

# Question:
# If area increases by 1 square foot:
# How much does predicted price increase?
# Use coefficient to explain.

# In your multiple linear regression pipeline, your model is trying to map out a function that looks like this
# predicted_price = (W1 * Area) + (w2 * Bedrooms) + (w3 * Age) + b

# after mathematically solved ; we get area is increases by w1 which is coeffiecent whihc is 131.60359534 , so if area increases by 1 square foot the predicted price will be increasesd with 131.60359534 


# custom prediction

# Area = 2100
# Bedrooms = 4
# Age = 3

# by the help of fomula : predicted_price = (W1 * Area) + (w2 * Bedrooms) + (w3 * Age) + b  and model coeef and interept value :
# we have :
#  [w1, w2, w3 ]  = [   131.60359534 -12793.07786869    405.72579844 ]

# using formula of  predicted_price : we get 
# predicted_price = (131.60359534 * 2100) + (-12793.07786869 * 4) + (405.72579844 * 3 ) + -67077.25311103676  =====> predicted_price =  159335.163024