for i in range(1,150):
    print("-", end="")
print("\t\t\t\t\t\tWelcome to Our Library Management System")
for i in range(1,150):
    print("-", end="")

books = {}

while True:
    userchoice = int(input("\nEnter any one option from the following given option/s\n 1: View Books List \n 2: Add Book \n 3: Remove Book \n 4: Search Book \n 5: Issue Book \n 6: Return Book \n 7: Exit \n"))

    if userchoice == 1:
        if not books:
            print("No books available")
        else:
            print("ID\tName\tAuthor\tStatus")
            for book_id, book_dtl in books.items():
                print(f"{book_id}\t{book_dtl['name']}\t{book_dtl['author']}\t{book_dtl['status']}")

    elif userchoice == 2:
        id_input = int(input("Enter Book ID (just number): "))
        book_id = "bk" + str(id_input)
        name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")
        status = "Available"
        books[book_id] = {
            "name": name,
            "author": author,
            "status": status
        }
        print("Book Added Successfully")

    elif userchoice == 3:
        id_input = int(input("Enter Book ID to Remove (just number): "))
        book_id = "bk" + str(id_input)
        if book_id in books:
            del books[book_id]
            print("Book Removed Successfully")
        else:
            print("Book not found")

    elif userchoice == 4:
        search = input("Enter Book Name to Search: ").lower()
        found = False
        print("ID\tName\tAuthor\tStatus")
        for book_id, book_dtl in books.items():
            if search in book_dtl['name'].lower():
                print(f"{book_id}\t{book_dtl['name']}\t{book_dtl['author']}\t{book_dtl['status']}")
                found = True
        if not found:
            print("Book Not Found")

    elif userchoice == 5:
        id_input = int(input("Enter Book ID to Issue (just number): "))
        book_id = "bk" + str(id_input)
        if book_id in books:
            if books[book_id]['status'] == "Available":
                books[book_id]['status'] = "Issued"
                print("Book Issued Successfully")
            else:
                print("Book is already issued")
        else:
            print("Book not found")

    elif userchoice == 6:
        id_input = int(input("Enter Book ID to Return (just number): "))
        book_id = "bk" + str(id_input)
        if book_id in books:
            books[book_id]['status'] = "Available"
            print("Book Returned Successfully")
        else:
            print("Book not found")

    elif userchoice == 7:
        print("Thank you for using our Library Management System")
        break

    else:
        print("Invalid Option. Try again.")