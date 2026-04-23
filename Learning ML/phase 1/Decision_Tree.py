from sklearn.tree import DecisionTreeClassifier


X = [[1],[2],[3],[4],[5],[6],[7],[8]]
y = [0,0,0,0,1,1,1,1]

model = DecisionTreeClassifier()

model.fit(X,y)

pred = model.predict(X)

for i, j in zip(pred, X) :
  print(f" {j}: {i}")

