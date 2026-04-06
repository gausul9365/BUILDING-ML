from sklearn.linear_model import LinearRegression

# X = [[1], [2], [3], [4]]
# # y = [2,4,6,8]
# # output data changes
# y = [3, 5, 7, 9]


# new data
X = [[1], [2], [3], [4]]
y = [2, 5, 7, 20]
model = LinearRegression()

model.fit(X,y)

# task 1 /task 2
print(model.coef_)
print(model.intercept_)

# 