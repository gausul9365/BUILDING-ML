import numpy as np

marks = np.array([
    [80, 90, 85],
    [60, 70, 65],
    [90, 95, 92]
])

# 1. Average per student (NO LOOPS)
      # axis = 0 → go down columns 
      # axis = 1 → go across rows 

avg = np.round(np.mean(marks, axis = 1), 2)

print(f"Avg: {avg}")

# 2. Find top student index
top = 0
for i in avg:
  if i > top:
    top = i
print(top)
# no loop
top_index = np.argmax(avg)
top_value = avg[top_index]

print(f"Top Index: {top_index}")
print(f"Top value : {top_value}")


# 3. Get students above threshold

result = []
for i in avg:
  if i > 80:
    result.append(float(i))

print(result)

# no loop
thresold = 80

filtered = avg[avg > thresold]
print(filtered)


# 1. Normalize marks (0–1 range)

def nomalize_marks(students):
  min = np.min(marks)
  max = np.max(marks)
  return [(x - min ) / (max - min) for x in students ]

print(nomalize_marks(marks))

# 2. Add 5 bonus marks to ALL students
bonus_marks = 5
print("wihout bonus marks: ", marks)
print("wihout bonus marks: ", marks + 5)

# 3. Find students whose ALL marks > 70
thresold_value = 70
def greaterThanThresold(marks):
  return [x [x > thresold_value] for x in marks ]

print("marks greater than 70: ", greaterThanThresold(marks))


# no loop

mask = np.all(marks > thresold_value, axis= 1)

thresold_marks = marks[mask]
print(thresold_marks)