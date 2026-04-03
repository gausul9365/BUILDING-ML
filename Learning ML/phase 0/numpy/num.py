import numpy as np

arr = np.array([1,2,3,4])
print(arr)

print(arr*2)
result = arr*3
print(np.mean(result))
print(np.sum(arr))

arr = arr.reshape(2,2)
print(arr)

print(arr[0])
print(arr[:,1])

print(arr.shape)