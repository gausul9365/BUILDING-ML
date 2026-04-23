from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score

X = [[1],[2],[3],[4],[5],[6],[7],[8]]
y = [0,0,0,1,1,1,0,0] 


model_tree = DecisionTreeClassifier()
model_linear = LogisticRegression()

# train 
model_tree.fit(X,y)
model_linear.fit(X,y)

pred_tree = model_tree.predict(X)
pred_linear = model_linear.predict(X)


# Print predictions and compare:
# logistic regression vs decision tree
print(pred_tree)
print(pred_linear)

# output i got 
# [0 0 0 1 1 1 0 0]
# [0 0 0 0 0 0 0 0]

# here we can clearly see the model output -  linear model get compeletely failed here and classified every datapoint as 0 which meansit can only give the best output on linear dataset but logistic regression gives the accurate data.


# let see the accuracy and precsion recall to understand them deeply 

acc_tree = accuracy_score(y, pred_tree)
acc_linear = accuracy_score(y, pred_linear)

print(f"tree_acc : {acc_tree}\n linear_acc: {acc_linear} ")
# tree_acc : 1.0
# linear_acc: 0.625 




# Task 3 (Critical Thinking) - Which model performs better here and WHY?
# decision tree has better performance then logistic regression 
# now we can clearly see decision tree has accuracy of 1 while logistic regression has 0.6 accuracy, now its clear that if data set is non linear then logistic regression gets failed coz it has one straight dicsion boundary which is unable to work on mulitple de


