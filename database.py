import json
import os


FILE = "data.json"


# Create database file

if not os.path.exists(FILE):

    with open(FILE, "w") as f:
        json.dump([], f)



# Read database

def load_data():

    with open(FILE, "r") as f:

        return json.load(f)



# Save database

def save_data(data):

    with open(FILE, "w") as f:

        json.dump(data, f, indent=4)



# Add Record

def add_record():

    data = load_data()


    id = input("Enter ID: ")

    name = input("Enter Name: ")

    age = input("Enter Age: ")

    course = input("Enter Course: ")



    record = {

        "id": id,
        "name": name,
        "age": age,
        "course": course

    }


    data.append(record)


    save_data(data)


    print("Record Added Successfully")




# View Records

def view_records():

    data = load_data()


    if len(data)==0:

        print("Database Empty")

    else:

        for record in data:

            print("----------------")

            print("ID:",record["id"])

            print("Name:",record["name"])

            print("Age:",record["age"])

            print("Course:",record["course"])




# Search Record

def search_record():

    data = load_data()


    search_id=input("Enter ID: ")


    for record in data:


        if record["id"] == search_id:


            print(record)

            return


    print("Record Not Found")




# Update Record

def update_record():

    data=load_data()


    id=input("Enter ID: ")


    for record in data:


        if record["id"] == id:


            record["name"] = input("New Name: ")

            record["age"] = input("New Age: ")

            record["course"] = input("New Course: ")



            save_data(data)


            print("Updated Successfully")

            return



    print("Record Not Found")





# Delete Record

def delete_record():

    data=load_data()


    id=input("Enter ID: ")



    for record in data:


        if record["id"] == id:


            data.remove(record)


            save_data(data)


            print("Deleted Successfully")

            return



    print("Record Not Found")





# Menu


while True:


    print("""
    
    ===== MINI DATABASE SYSTEM =====

    1. Add Record

    2. View Records

    3. Search Record

    4. Update Record

    5. Delete Record

    6. Exit

    """)



    choice=input("Enter Choice: ")



    if choice=="1":

        add_record()


    elif choice=="2":

        view_records()


    elif choice=="3":

        search_record()


    elif choice=="4":

        update_record()


    elif choice=="5":

        delete_record()


    elif choice=="6":

        print("Exit Database")

        break


    else:

        print("Invalid Choice")
