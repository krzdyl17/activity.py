class Book:
 
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2 = Book("Invisible Man", "Ralph Ellison", 1952)
book3 = Book("Things Fall Apart", "Chinua Achebe", 1958)

book1.describe()
print()
book2.describe()
print()
book3.describe()
