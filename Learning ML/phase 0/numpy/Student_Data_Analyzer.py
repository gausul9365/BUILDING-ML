
students = [
    {"name": "A", "marks": [80, 90, 85]},
    {"name": "B", "marks": [60, 70, 65]},
    {"name": "C", "marks": [90, 95, 92]}
]

  
def avg_stu(data):
    return [sum (row["marks"]) / len(row["marks"])  for row in  data]
  
def calculate_average(student):
    return sum(student["marks"]) / len(student["marks"])
  

def find_top_student(students):
    
    top_student = None
    highest = 0

    for student in students:
      avg = calculate_average(student)
      if avg > highest :
        highest = avg
        top_student = student
    
    return top_student

def students_above_threshold(students, threshold):
    result = []

    for student in students:
        avg = calculate_average(student)
        if avg > threshold:
            result.append(student)

    return result


print(avg_stu(students))


print(find_top_student(students))  

print(students_above_threshold(students, 80))  


    