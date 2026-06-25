import json
import os


FILE = "students.json"


# Create database file

if not os.path.exists(FILE):

    with open(FILE, "w") as f:
        json.dump([], f)



# Load Students

def load_students():

    with open(FILE, "r") as f:

        return json.load(f)



# Save Students

def save_students(data):

    with open(FILE, "w") as f:

        json.dump(data, f, indent=4)




# CREATE - Add Student

def add_student():

    students = load_students()


    roll = input("Enter Roll Number: ")


    # check duplicate

    for s in students:

        if s["roll"] == roll:

            print("Student already exists")

            return



    name = input("Enter Name: ")

    age = input("Enter Age: ")

    course = input("Enter Course: ")



    student = {

        "roll": roll,

        "name": name,

        "age": age,

        "course": course

    }



    students.append(student)


    save_students(students)


    print("Student Added Successfully")





# READ - View Students

def view_students():

    students = load_students()



    if len(students)==0:

        print("No Records Found")

        return



    print("\n----- Student Records -----")



    for s in students:

        print("----------------")

        print("Roll:",s["roll"])

        print("Name:",s["name"])

        print("Age:",s["age"])

        print("Course:",s["course"])





# SEARCH Student

def search_student():

    students = load_students()


    roll=input("Enter Roll Number: ")



    for s in students:


        if s["roll"] == roll:


            print("\nStudent Found")

            print(s)

            return



    print("Student Not Found")






# UPDATE Student

def update_student():

    students = load_students()


    roll=input("Enter Roll Number: ")



    for s in students:


        if s["roll"] == roll:


            s["name"] = input("New Name: ")

            s["age"] = input("New Age: ")

            s["course"] = input("New Course: ")



            save_students(students)


            print("Updated Successfully")

            return



    print("Student Not Found")







# DELETE Student

def delete_student():

    students = load_students()


    roll=input("Enter Roll Number: ")



    for s in students:


        if s["roll"] == roll:


            students.remove(s)


            save_students(students)


            print("Deleted Successfully")

            return



    print("Student Not Found")






# MAIN MENU


while True:


    print("""
    
    ===== STUDENT RECORD MANAGEMENT =====


    1. Add Student

    2. View Students

    3. Search Student

    4. Update Student

    5. Delete Student

    6. Exit

    """)



    choice=input("Enter Choice: ")




    if choice=="1":

        add_student()



    elif choice=="2":

        view_students()



    elif choice=="3":

        search_student()



    elif choice=="4":

        update_student()



    elif choice=="5":

        delete_student()



    elif choice=="6":

        print("Program Closed")

        break



    else:

        print("Invalid Choice")
