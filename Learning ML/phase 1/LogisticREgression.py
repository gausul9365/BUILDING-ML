from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# data
X = [[1], [2], [3], [4], [5]]
y = [0,0,0,1,1] 
Y = [[1], [2], [12], [3],[14]]
# model 
model = LogisticRegression()
  
# train
model.fit(X,y)

# predict probability
probability = model.predict_proba(X) 

# predict classes
pred_class = model.predict(Y)


# Accuracy
acc = accuracy_score(y, pred_class)


print("Probabilities:\n", probability)
print("Predictions:", pred_class)
print("Accuracy:", acc)


