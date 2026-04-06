from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4]]
y = [2,4,6,8]

model = LinearRegression()

model.fit(X,y)

predict = model.predict([[5], [10]])

print(predict)

print(model.coef_)

print(model.intercept_)