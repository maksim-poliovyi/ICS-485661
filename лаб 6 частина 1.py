import pandas as pd
dataFile = "dataFileHomeLibrary.txt"


class Library():

    books = []

    def __init__(self, name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year
        

print(Library.books)


print("The Home Library welcomes you")

while True:

    print("0. Exit\n1. Print the home library\n2. Search for book\n")
    userInput = str(input())
    

    if userInput == "0":
        break


    elif userInput == "1":
        library1 = pd.read_csv(dataFile)
        print(library1.to_string()+"\n")
        

    elif userInput == "2":

        print("Enter keyword to search\n")
        keyWord1 = str(input())

        file4 = open(dataFile, "r+").readlines()
        for line in file4:
            Library.books.append(line)
            
        for book1 in Library.books:
            if keyWord1 in book1:
                print(book1)


    else:
        print("Invalid Input\n")