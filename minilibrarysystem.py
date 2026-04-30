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

def updateBook():
    try:
        with open("library.txt", "r") as file:
            books = [line.strip() for line in file.readlines()]

        if not books:
            print("The library is empty")
            return
        
        print("\n--=Books in the Library=--")
        for index, book in enumerate(books, start=1):
            print(f"{index}. {book}")

        try:
            choice = int(input("Enter the number of the book to update: "))

            if 1<= choice <= len(books):
                newName = input("Enter new name: ")
                oldName = books[choice-1]
                books[choice - 1] = newName
                
                with open("library.txt", "w") as file:
                    for book in books:
                        file.write(book + "\n")
                
                print(f"Successfully updated '{oldName}' to '{newName}'")
            else:
                print("Invalid number selection.")

        except ValueError:
            print("Please enter a valid number.")

    except ValueError:
        print("Please enter a valid number.")
    except FileNotFoundError:
        print("Library file not found.")

def removeBooks():
    try:
        with open("library.txt", "r") as file:
            books = file.read().splitlines()
            print("\n--=Books in the Library=--")
            print(books)

            remove = input("Enter book to delete: ")
            if remove not in books:
                print("Book doesn't exist")
                return

            with open("library.txt", "w") as file:
                for book in books:
                    if book == remove:
                        print(f"{book} succesfully removed")
                    else:
                        file.write(book + '\n')
            print("Update Complete\n")
    except:
        print("An error occured")
        
while True:
    print("MINI LIBRARY SYSTEM")
    print("1. Add Book")
    print("2. View Books")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Exit")
    try: 
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addBook()

        elif choice == 2:
            viewBooks()
            
        elif choice == 3:
            updateBook()
        
        elif choice == 4:
            removeBooks()

        elif choice == 5:
            print("Exiting the program....")
            break

        else: 
            print("Invalid choice. Please try again.")

    except ValueError:
        print("Invalid input. Please enter a number.")

    