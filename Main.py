from CRUD_Operation import CRUD

def main():
    db = CRUD()
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
            if(choice == 1):
                id = int(input("Enter student Id: "))
                name = input("Enter student name: ")
                phoneno = input("Enter student phone number: ")
                db.insert(id, name, phoneno)

            elif choice == 2:
                db.select()
                
            elif choice == 3:
                id = int(input("Enter Student id you want to delete"))
                db.delete(id)

            elif choice == 4:
                id = int(input("Enter student Id: "))
                name = input("Enter New student name: ")
                phoneno = input("Enter New student phone number: ")
                db.update(id, name, phoneno)
            elif choice == 5:
                break
            else:
                print("Invalid Input....")
        except Exception as e:
            print("Invalid Input!!! ", e)

if __name__ == '__main__':
    main()