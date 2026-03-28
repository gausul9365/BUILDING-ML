students = [
    {"name": "A", "marks": [80, 90, 85]},
    {"name": "B", "marks": [60, 70, 65]},
    {"name": "C", "marks": [90, 95, 92]}
]


def calculate_average(student):
    return sum(student["marks"]) / len(student["marks"])


def enrich_students_with_avg(students):
    enriched = []
    for student in students:
        avg = calculate_average(student)
        enriched.append({
            "name": student["name"],
            "marks": student["marks"],
            "average": avg
        })
    return enriched


def find_top_student(students):
    return max(students, key=lambda x: x["average"])


def students_above_threshold(students, threshold):
    return [s for s in students if s["average"] > threshold]

def sort_student_average(students):
    return sorted( students, key = lambda x:x["average"], reverse= True )



def class_average(students):
    
    total = sum( s["average"] for s in students)
    return total / len(students)

def print_report(students):
    for s in students:
        print(f"Name: {s['name']} | Avg: {round(s['average'], 1)}")

# ---- PIPELINE ----

enriched_students = enrich_students_with_avg(students)

top_student = find_top_student(enriched_students)

filtered_students = students_above_threshold(enriched_students, 80)
avg_class = class_average(enriched_students)
sorted_students = sort_students_by_average(enriched_students)
print_report(sorted_students)

print("Enriched Data:", enriched_students)
print("Top Student:", top_student)
print("Above Threshold:", filtered_students)