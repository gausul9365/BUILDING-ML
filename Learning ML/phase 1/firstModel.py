X = [1,2,3,4]
Y = [2,4,6,8]

w = 0
b = 0
lr = 0.01

for epoch in range(1000):
  total_error = 0

  for i in range(len(X)):

    x = X[i]
    y = Y[i]

    # code model 
    y_predict = w * x + b
    error = y_predict - y

    # gradients

    db = error
    dw = error * x

    # update

    w = w - lr * dw
    b = b - lr * db

    print(f"{epoch} : {w, b}") 

