class Book:
    def __init__(self, title, author, pages, genre):
        # Initialize book attributes
        #added Genres
        self.title = title
        self.author = author
        self.pages = pages
        self.genre=genre
        self.read = False  
        #purchase count 
        self.purchase_count=0

    def description(self):
        # Return book details
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages},Genre:{self.genre},Purchased: {self.purchase_count} times"

    def mark_as_read(self):
        # Mark the book as read and print a message
        self.read = True
        print(f"You have marked '{self.title}' as read.")

class EbookReader:
    def __init__(self):
        # Predefined list of available books
        self.available_books = [
            Book("The Little Liar", "Mitch Albom", 279,"Fiction"),
            Book("Moby Dick", "Herman Melville", 635, "Classic"),
            Book("The Hunger Games", "Suzanne Collins", 358, "Fanasty"),
            Book("Frankenstein", "Mary Shelley", 280, "Horror"),
            Book("The Keeper", "Buck Turner", 320, "Thriller"),
        ]
        self.purchased_books = []  

#add method to filter book by genre

    def display_genres(self):
        # Display genres from available books
        genres = set(book.genre for book in self.available_books)
        print("Available Genres:")
        for genre in genres:
            print(f"- {genre}")

    def filter_books_by_genre(self, selected_genre):
        # Display books filtered by users genre
        print(f"Books in {selected_genre} genre:")
        filtered_books = [book for book in self.available_books if book.genre.lower() == selected_genre.lower()]
        if filtered_books:
            for book in filtered_books:
                print(book.description())
        else:
            print(f"No books found in the genre: {selected_genre}")



    def display_available_books(self):
        # Print the list of available books
        print("Available Books:")
        for index, book in enumerate(self.available_books):
            print(f"{index + 1}. {book.description()}")

    def buy_book(self, index):
        # Buy a book by index
        if 0 <= index < len(self.available_books):
            # Remove from available
            book = self.available_books.pop(index) 
            #track how many times each book has been purchased
            book.purchase_count += 1
            # Add to purchased list
            self.purchased_books.append(book)  
            print(f"You have purchased '{book.title}'.")
        else:
            print("Invalid book index.")

    def view_purchased_books(self):
        # Print the list of purchased books
        if not self.purchased_books:
            print("You have not purchased any books yet.")
            return
        print("Your Purchased Books:")
        for book in self.purchased_books:
            print(book.description())

    def read_book(self, index):
        # Mark purchased books as read 
        if 0 <= index < len(self.purchased_books):
            book = self.purchased_books[index]
            book.mark_as_read()
        else:
            print("Invalid book index.")
# display top 3 po=urchasd books
    def top_purchased_book(self):
        sorted_books = sorted(self.available_books + self.purchased_books, key=lambda book: book.purchase_count, reverse=True)
        print("The top 3 most purchased Booka are:")
        for book in sorted_books[:3]:
            print(book.description())
        
#search by author 
    def search_by_author(self,author_name):
        print(f"Books by {author_name}:")
        found_books = [book for book in self.available_books + self.purchased_books if book.author.lower() == author_name.lower()]
        if found_books:
            for book in found_books:
                print(book.description())
        else:
            print("No books found by that author.")

#search by title
    def search_by_title(self, title):
        sorted_books = sorted(self.available_books + self.purchased_books, key=lambda book: book.title.lower())
#binary search for title 
        low, high = 0, len(sorted_books) - 1
        while low <= high:
            mid = (low + high) // 2
            if sorted_books[mid].title.lower() == title.lower():
                print(f"Found: {sorted_books[mid].description()}")
                return
            elif sorted_books[mid].title.lower() < title.lower():
                low = mid + 1
            else:
                high = mid - 1

        print("Book not found.")

#Save and load Purchases 
    def save_purchasers(self, filename='purchase.txt'):
        #save purchased books to a txt file 
        with open(filename, 'w') as file:
            for book in self.purchased_books:
                file.write(f"{book.title},{book.author},{book.pages},{book.genre},{book.purchase_count}\n")
        print("Purchased books saved.")

    def load_purchases(self, filename='purchases.txt'):
        #load from txt
        try:
            with open(filename, 'r') as file:
                for line in file:
                    title, author, pages, genre, purchase_count = line.strip().split(',')
                    book = Book(title, author, int(pages), genre)
                    book.purchase_count = int(purchase_count)
                    self.purchased_books.append(book)
            print("Purchased books loaded.")
        except FileNotFoundError:
            print("No saved purchases found.")





  

def main():
    reader = EbookReader()  
    #load purchases 
    reader.load_purchases()


    while True:
        # Display menu options
        print("\nE-Book Reader Menu:")
        print("1. Display Available Books")
        print("2. Buy a Book")
        print("3. View Purchased Books")
        print("4. Read a Book")
        print("5. Display Available Genres")
        print("6. Filter Books by Genre")
        print("7. Search by Author")
        print("8. Search by Title")
        print("9. Top Purchased Books")
        print("10. Save Purchases")
        print("11. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            reader.display_available_books()  
        elif choice == '2':
            reader.display_available_books()  
            book_index = int(input("Enter the number of the book you want to buy: ")) - 1
            reader.buy_book(book_index)  
        elif choice == '3':
            reader.view_purchased_books()  
        elif choice == '4':
            reader.view_purchased_books()  
            book_index = int(input("Enter the number of the book you want to read: ")) - 1
            reader.read_book(book_index)  
        elif choice == '5':
            reader.display_genres()  
        elif choice == '6':
            reader.display_genres()
            genre = input("Enter a genre to filter by: ")
            reader.filter_books_by_genre(genre)
        elif choice == '7':
            author = input("Enter the author's name: ")
            reader.search_by_author(author)
        elif choice == '8':
            title = input("Enter the title of the book: ")
            reader.search_by_title(title)
        elif choice == '9':
            reader.top_purchased_books()
        elif choice == '10':
            reader.save_purchases()
        elif choice == '11':
            print("Exiting the e-book reader.")  
            break
        else:
            print("Invalid option, please try again.") 

# Run the main function
if __name__ == "__main__":
    main() 

