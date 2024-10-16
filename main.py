class Books:
    def __init__ (self,title,author,pages,read,owned):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False
        self.owned = False

b1 = Books("Enders Game","Orson Scott Card","256",False,False)
b2 = Books("Ready Player One", "Ernest Cline", "348",False,False)

availableList = [b1,b2]
purchasedList = []
readList = []

def updateLists(avail,purch,read):
    
    for book in avail:
        i = 0
        if avail[i].owned == True:
            purch.append(avail[i])
        i+=1
    for book in purch:
        i=0
        if purch[i].owned == True:
            read.append(purch[i])
        i+=1
        


def desctiption(book):
    print("Title: " + book.title + " Author: " + book.author + " Pages: " + book.pages )

def mark_as_read(book):
    book.read = True
    print("You have finished reading " + book.title + ".")

def menu(available,purchased,read):
    con = True
    while con == True:
        print("USER MENU (input the number to select option)")
        print("1. Display books availabe")
        print("2. Display books purchased")
        print("3. Display books read")
        print("4. EXIT")
        inp = input("Choose an option ")
        if inp == "1":
            i = 0
            for books in available:
                print(available[i].title)
                i+=1
            updateLists(available,purchased,read)
        elif inp == "2":
            print(purchased)
            updateLists(available,purchased,read)
        elif inp == "3":
            print(read)
            updateLists(available,purchased,read)
        elif inp == "4":
            break
            
menu(availableList,purchasedList,readList)