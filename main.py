import json 


class BookCollection: 
    """A class to manage the colelction of books, allwing the users to organise teh library"""
    
    def __init__(self):
        self.books_list = []
        self.storage_file = "books_json.json"
        self.read_from_files()

    def read_from_files(self):
        """Load save book from json file into memory"""
        try:
            with open(self.storage_file, "r") as file:
                self.books_list = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            self.books_list = []
            print("No saved books found")
            
    def save_to_file(self):
        """Save books from memory to json file"""
        with open(self.storage_file, "w") as file:
            json.dump(self.books_list, file, indent=4)

    def create_new_book(self):
        """Create a new book and add it to the collection"""
        title:str = input("Enter the title of the book: ")
        author: str = input("Enter the author of the book: ")
        publication_year: int = input("Enter the year the book was published: ") 
        gener:str = input("Enter the gener of the book:")
        is_book_read =( input("Have you read the book? (yes/no): ").strip().lower() == "yes")
        
        new_book = {
            "title": title,
            "author": author,
            "publication_year": publication_year,
            "gener": gener,
            "is_book_read": is_book_read
    }

        self.books_list.append(new_book)
        self.save_to_file()
        print("Book added successfully\n")



    def delete_book(self):
        """Delete a book from the collection"""

        print("List of the books in the library")
        for index, book in enumerate(self.books_list):
            print(f"{index + 1}. {book['title']} by {book['author']}")
            title = input("Enter the title of the book you want to delete: ")
            author = input("Enter the name of the author fo the book you want to delete: ")

        for book in self.books_list:
            if book["title"] == title and book["author"] == author:
               self.books_list.remove(book)
               self.save_to_file()
               print("Book deleted successfully")
               return
                        
            print("Book not found")




    def List_of_read_books(self):
         print("List of the read books in the library")
         for index, book in enumerate(self.books_list):
              
              if book["is_book_read"] == True:
                print(f"{index + 1}. {book['title']} by {book['author']}, read\n {book['is_book_read']}");
              else:
                print("No read books found")
                return

    def search_book(self):

        search =  input("Enter the name of the book you want to search:\n 1. title\n 2. author\n ehter title or author: ")
        for index, book in enumerate(self.books_list):
              
              if search == book["title"] or search == book["author"]:
                print(f"Here is your search result\n: {index + 1}. title of the book: {book['title']}, written by {book['author']}, read:{book['is_book_read']}");
              else:
                    print("Book not found")

    def list_all_books(self):
        print("List of all books in the library")
        while True:
            for index, book in enumerate(self.books_list):
             print(f"{index + 1}. {book['title']} by {book['author']}")
            break

    def edit_book_title(self):
        """Edit the title of a book"""
     
        
        try:
            book_index = int(input("\nEnter the number of the book to edit: ")) - 1
            if book_index < 0 or book_index >= len(self.books_list):
                print("Invalid selection. Please try again.")
                return
            
            new_title = input("Enter the new title: ").strip()
            if not new_title:
                print("Title cannot be empty.")
                return
            
            self.books_list[book_index]["title"] = new_title
            self.save_to_file()
            print("Book title updated successfully!")

        except ValueError:
            print("Invalid input. Please enter a number.")


    def percentage_of_read_books(self):
     """Calculate and display the percentage of books that have been read."""
     if not self.books_list:
         print("No books in the library.")
         return
    
     read_books = sum(1 for book in self.books_list if book["is_book_read"])  # Count read books
     total_books = len(self.books_list)

     if read_books == 0:
        print("No read books found.")
     else:
        percentage = (read_books / total_books) * 100
        print(f"Percentage of read books: {percentage:.2f}%")
 

    def quit(self):
        """Save books to file and exit the program"""
        self.save_to_file()
        print("Goodbye!")
        exit

    def start(self):
        
        while True:
            print("Welcome to the Library Manager")
            print("Choose an option:")
            print("1. Add a new book")
            print("2. remove a book")
            print("3. List of all read books")
            print("4. Search any book!")
            print("5. List of All books!")
            print("6.Edit book title!")
            print("7.percentage of read books!")
            print("8.Exit!!")
            user_choise = input("please choose an option from 1-4 : ")

            if user_choise == "1":
             self.create_new_book()
             
            elif user_choise == "2":
                self.delete_book()
            elif user_choise == "3":
                self.List_of_read_books()
            elif user_choise == "4":
                self.search_book()
            elif user_choise == "5":
                self.list_all_books()
            elif user_choise == "6":
                self.edit_book_title()
            elif user_choise == "7":
                self.percentage_of_read_books()
            elif user_choise == "8":
                self.quit()
            else:
                print("book not found!!")
            break

if __name__ == "__main__":
    book_collection = BookCollection()
    book_collection.start()
