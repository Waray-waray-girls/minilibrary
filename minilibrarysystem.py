try:
    with open("library.txt", "x") as file:
        print("File succesfully created")
except FileExistsError:
    print("File Already Exists")
except:
    print("An error occured")

def addBook():
    with open("library.txt", "a") as file:
        book = input("Enter book to add: ")
        file.write(book + "\n")
        print(f"{book} added succesfully")


while True:
    print("MINI LIBRARY SYSTEM")
    print("1. Add Book")
    print("2. Exit")
    try: 
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addBook()

        elif choice == 2:
            print("Exiting the program....")
            break

        else: 
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")