# # Build a model to predict:
# # Pass / Fail based on study hours
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Data
data = {
    "hours": [1,2,3,4,5,6,7,8],
    "pass":  [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

# Features & Target
X = df[["hours"]]
y = df["pass"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)

# Evaluation
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)

# Output
print("Predictions:", y_pred)
print("Actual:", y_test.values)
print("Probabilities:\n", y_prob)

print(f"\nAccuracy: {acc}")
print(f"Precision: {prec}")
print(f"Recall: {rec}")

print(model.coef_)
print(model.intercept_)





 

# import pandas as pd 
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import accuracy_score, precision_score, recall_score
# data = {
#     "hours": [1,2,3,4,5,6,7,8],
#     "pass":  [0,0,0,0,1,1,1,1]
# }

# df = pd.DataFrame(data)

# X = df[["hours"]]
# y = df["pass"]
# model_test = LogisticRegression()

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)
# model_test.fit(X_train, y_train)

# pred_test= model_test.predict(X_test)

# print(f"prediction on test data: {pred_test}")
# print(f"Actual result: {y_test.values}")



# model = LogisticRegression()

# model.fit(X, y)

# predicted = model.predict(X)
# prob = model.predict_proba(X)

# print(predicted)
# print(prob)


# # printing accuracy, precision, recall
# acc = accuracy_score(y, predicted)
# prec = precision_score(y, predicted)
# rec = recall_score(y, predicted)

# print(f"Accuracy: {acc}  | Precision : {prec}  | Recall: {rec}")



