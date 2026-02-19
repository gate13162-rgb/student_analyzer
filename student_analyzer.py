

def process_scores(student , marks):
    total_score = sum(marks)
    average_score = total_score / len(marks)
    return student, average_score

def classify_performance(average_score):
    if average_score >= 90:
        return "A"
    elif average_score >= 75:
        return "B"
    elif average_score >= 60:
        return "C"
    else:
        return "F"
    
def status(average_score):
    if average_score >= 60:
        return "Pass"
    else:
        return "Fail"

num_list = []
print("Enter the no of students")
num_students = int(input())
name_list = []
students = []
for i in range(num_students):
    print(f"Enter details for student {i+1}")
    student = input("Enter the name of student:")
    name_list.append(student)
    print("Enter the marks of 5 subjects within 100: ")
    
    for i in range(5):
        mark = float(input(f"Enter mark for subject {i+1}: "))
        num_list.append(mark)
    
    student, average_score = process_scores(student, num_list)
    grade = classify_performance(average_score)
    status1 = status(average_score)
    students.append({"name": student, "average": average_score, "grade": grade, "status": status1})

print("\n =====Student Performance Analysis:======")   
for student in students:
    print(f"{student['name']} | Avg : {student['average']:.2f} | Grade :{student['grade']} | Status : {student['status']} ")

print("\n total students : ", num_students)
pass_count = 0
fail_count = 0
for student in students:
    if student['status'] == "Pass":
        pass_count += 1
print("total pass students : ", pass_count)
for student in students:
    if student['status'] == "Fail":
        fail_count += 1

print("total fail students : ", fail_count)