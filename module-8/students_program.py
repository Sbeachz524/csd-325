import json

# Load the JSON file into a Python list
with open("Student.json", "r") as file:
    student_list = json.load(file)

def print_students(students):
    for s in students:
        print(f"{s['L_Name']}, {s['F_Name']} : ID = {s['Student_ID']} , Email = {s['Email']}")

print("This is the original Student list:")
print_students(student_list)

# Add your information to the list
new_student = {
        "F_Name": "Zi",
        "L_Name": "Beacham",
        "Student_ID": 210208,
        "Email": "aqua3894@gmail.com"

}

student_list.append(new_student)

print("This is the updated Student List:")
print_students(student_list)

#Write the updated list back to the JSON file
print("Writing to JSON now...")
with open("Student.json", "w") as file:
        json.dump(student_list, file, indent=4)

print("The Student.json file has been updated.")
