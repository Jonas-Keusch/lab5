class Books: #create books class
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False
        self.owned = False

# book options
b1 = Books("Ender's Game", "Orson Scott Card", 256)
b2 = Books("Ready Player One", "Ernest Cline", 348)
b3 = Books("The Hobbit", "J.R.R. Tolkien", 310)

#create lists
availableList = [b1, b2, b3]
purchasedList = []
readList = []

#update lists after user actions
def updateLists(avail, purch, read):
    purch.clear()
    read.clear()
    for book in avail:
        if book.owned:
            purch.append(book)
            if book.read:
                read.append(book)

def description(book):
    print(f"Title: {book.title}, Author: {book.author}, Pages: {book.pages}")

#marks books as read
def mark_as_read(book):
    book.read = True
    print(f"You have finished reading {book.title}.")

#main user interaction menu
def mainMenu(available, purchased, read):
    while True:
        print("\nUSER MENU (input the number to select an option)")
        print("1. Display books available")
        print("2. Display books purchased")
        print("3. Display books read")
        print("4. EXIT")
        inp = input("Choose an option: ")

        if inp == "1":#if input is available books
            for i, book in enumerate(available):
                print(f"{i + 1}. {book.title}")
            availMenu(available)
            updateLists(available, purchased, read)

        elif inp == "2": #if input is purchased books
            print("\nPurchased Books:")
            for i, book in enumerate(purchased):
                description(book)
            purchMenu(purchased)
            updateLists(available, purchased, read)

        elif inp == "3": #if input is read books
            print("\nBooks Read:")
            for book in read:
                description(book)
            readMenu(readList)
            updateLists(available, purchased, read)

        elif inp == "4": #exit application
            break

def availMenu(avail): #menu if available is chosen
    inp = input("Choose a Book (number): ")
    try:
        selected_index = int(inp) - 1
        if 0 <= selected_index < len(avail):
            print(f"Would you like to purchase {avail[selected_index].title}?")
            print("1. Yes")
            print("2. No")
            inp2 = input()
            if inp2 == "1":
                avail[selected_index].owned = True
                updateLists(availableList, purchasedList, readList)
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

def purchMenu(purch): #menu if purchased is chosen
    inp = input("Choose a Book (number): ")
    try:
        selected_index = int(inp) - 1
        if 0 <= selected_index < len(purch):
            print("1. Mark as read")
            print("2. Open book")
            print("3. Back to menu")
            inp2 = input("Choose an option: ")
            if inp2 == "1":
                mark_as_read(purch[selected_index])
            elif inp2 == "2":
                print(f"Opening {purch[selected_index].title}...")
            elif inp2 == "3":
                print("Returning to Menu")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")
 
def readMenu(read):
    inp = input("Choose a Book (number): ")
    try:
        selected_index = int(inp) - 1
        if 0 <= selected_index < len(read):
            print("1. Read book again")
            print("2. Mark as unread")
            print("3. Back to menu")
            inp2 = input("Choose an option: ")
            if inp2 == "1":
                print(f"Opening {read[selected_index].title}...")
            elif inp2 == "2":
                read[selected_index].read = False
            elif inp2 == "3":
                print("Returning to Menu")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a valid number.")

mainMenu(availableList, purchasedList, readList)