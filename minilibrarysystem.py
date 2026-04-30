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