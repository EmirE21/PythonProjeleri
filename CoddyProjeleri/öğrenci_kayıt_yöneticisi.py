student_records = {}

def add_student(name, age, courses):
    courses_set = set(courses)
    if name in student_records.keys():
        print(f"Student '{name}' already exists.")
    else:
        student_records[name] = {
            "age": age,
            "grades": set(),
            "courses": courses_set
        }
        print(f"Student '{name}' added successfully.")
        
def add_grade(name, grade):
    if name not in student_records.keys():
        print(f"Student '{name}' not found.")
    else:
        student_records[name]["grades"].add(grade)
        print(f"Grade {grade} added for student '{name}'.")
        
def is_enrolled(name, course):
    if name not in student_records.keys():
        print(f"Student '{name}' not found.")
        return False
    if course in student_records[name]["courses"]:
        return True
    else:
        return False
    
def calculate_average_grade(name):
    if name not in student_records.keys():
        print(f"Student '{name}' not found.")
        return None
    grades = student_records[name]["grades"]
    if not grades:
        return 0
    total_grade = sum(grades)
    average = total_grade / len(grades)
    return float(average)

def list_students_by_course(course):
    name_list = []
    for name, name_info in student_records.items():
        if course in name_info["courses"]:
            name_list.append(name)
    return name_list

def filter_top_students(threshold):
    name_list = []
    for name in student_records.keys():
        if calculate_average_grade(name) > threshold:
            name_list.append(name)
    return name_list