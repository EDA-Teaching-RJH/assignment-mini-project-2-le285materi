import re
import csv
import os
# a librarymanager class made to manage a library system.
class librarymanager: 
    """This class is used to keep a record of the library's books.
    It has 3 modules: "Add books", "Return books", "Search Books". """
    libraryname = "" 
    listofbooks = ""

    def __init__ (self, libraryname):
        self.libraryname = libraryname #stores the libraries name as a variable 
        self.listofbooks= "Listofbooks.txt" #where the list of books file is stored

      #to display the list of books!
    def displaybooks(self):
        print( "List of books ") 
        bookList = open("Listofbooks.txt", "r")#opens the list of books from the file Listofbooks.txt
        print(bookList.read()) #opens file in read mode
        bookList.close() #closes the file

    #a regex function that searches through the Listofbooks.txt file to match the word the user searched with the words in the file
    def searchBooks(self):
        #ask the user to input the word they want to search for
        searchword = input("Add the word you would like to search for: ").strip()
        #open the file 
        book = open("Listofbooks.txt", "r") 
        lines = book.readlines()  #read all the  lines from file
        searchwordpattern = rf"\b{re.escape(searchword)}\b" #the pattern to search in the file
        found = False  #to track if the word is found
        for line in lines:
            #search for the word in each line of the file
            if re.search(searchwordpattern, line, re.IGNORECASE): #ignore all cases so there are no errors
                print(f"Word found in: {line.strip()}")
                found = True
        #if the searched word was not found in the file
        if not found:
            print(f"The word '{searchword}' was not found in the book list.")
        book.close()  #close the file

    #class module for the user to add books and an author to the file!
    def addbooks (self):
        books=input("Enter the title of the book:") # ask user to enter the book title
        Author=input("Enter the Authors name:") #ask user to enter the authors name
        if books==""or Author=="":  #check if the books or author is left as an empty string
            print("this is an invalid book name or author name")
        else:
            bookfile = open("Listofbooks.txt", "a") #open file in apend mode
            bookfile.write(f"{books}, {Author}") #add the new book title and author to the existing list of books
            print(f"The book '{books}' has been added successfully") 
            bookfile.close() #close the file

if __name__ == "__main__":
    try:
        library = librarymanager("Python's Library") 
        keylist = {"D": "display books", "A": "add books", "Q": "quit", "S": "search"} #the key commands for user to select from
        keypress = input("press enter") #press enter before choosing from the key commands
        while keypress.lower() != "q": #continue until user chooses to quit
            print(f"\nWelcome to {library.libraryname} library management system") # 
            for key, value in keylist.items(): #display avalible options for user
                print(f"Press {key} to {value}")
            keypress = input("Press key: ").lower() #convert to lowercase
            match keypress: #match users chosen input to avalible key commands
                case "a":
                    print("\nCurrent section: add books\n")
                    library.addbooks()
                case "d":
                    print("\nCurrent section: display books\n")
                    library.displaybooks()
                case "s":
                    print("\nCurrent section: searchBooks\n")
                    library.searchBooks()
                case "q":
                    print("\nCurrent section: quitting system\n")
                    break
                case _:
                    print("Option not available. Please try again.")
    except Exception as e: #to handle unexpected errors
        print("There was an error. Try again.")
        print(e)

       



        


            

              



