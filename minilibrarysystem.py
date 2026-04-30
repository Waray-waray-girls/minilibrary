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

def viewBooks():
    with open("library.txt", "r") as file:
        books = file.read()
        print("\n--=Books in the Library=--")
        print(books)


while True:
    print("MINI LIBRARY SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")
    try: 
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addBook()

        elif choice == 2:
            viewBooks()
            
        elif choice == 3:
            print("Exiting the program....")
            break

        else: 
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    