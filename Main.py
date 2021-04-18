'''
Author: Suraj N Temkar
Date: 15/04/2021
Title: Perform CRUD Operations 
'''

from CRUD_Operation import CRUD # import module of CRUD_Operations

def main():
    db = CRUD()     # Create object of the CRUD class
    while True:
        print("********Welcome***********")
        print()
        print("Press 1 to insert new Student")
        print("Press 2 to display all students")
        print("Press 3 to delete Student")
        print("Press 4 to update Student")
        print("Press 5 to Exit")
        print()
        try:
            choice = int(input())
            if(choice == 1):    # Insert 
                id = int(input("Enter student Id: "))
                name = input("Enter student name: ")
                phoneno = input("Enter student phone number: ")
                db.insert(id, name, phoneno)

            elif choice == 2:   # Select
                db.select()
                
            elif choice == 3:   # Delete
                id = int(input("Enter Student id you want to delete"))
                db.delete(id)

            elif choice == 4:   # Update
                id = int(input("Enter student Id: "))
                name = input("Enter New student name: ")
                phoneno = input("Enter New student phone number: ")
                db.update(id, name, phoneno)

            elif choice == 5:   # Exit
                break

            else:
                print("Invalid Input....")

        except Exception as e:
            print("Invalid Input!!! ", e)

# Main method
if __name__ == '__main__':
    main()