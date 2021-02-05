class Book:
    def __init__(self, name, pages):
        self.name= name
        self. pages = pages
        
    def __str__(self):
        return "Name: " + self.name + " Pages: " + self.pages 
    def __repr__(self):
        return "Name: " + self.name + " Pages: " + self.pages
        
class Backpack:
    def __init__(self, books):
        self.books = books

    def __str__(self):
        return books.__str()

    def __repr__(self):
        return books.__str()

    def __iter__(self):
        self.x = 0
        return self
    def __next__(self):
        if (self.x < len(self.books)):
            current_book = self.books[self.x]
            self.x = self.x+1
            return current_book
        else:
            raise StopIteration
            
b1 = Book("Hunger Games", "374 pages")
b2 = Book("Diary of a Wimpy Kid: Rodrick Rules", "217 pages")
b3 = Book("The Maze Runner", "375 pages")
b4 = Book("The Maze of Bones", "478 pages")
books = [b1, b2, b3, b4]

backpack_contents= Backpack(books)

print("--> Calling internal iterator")
for x in backpack_contents:
    print(x)
    
iterator_x = iter(backpack_contents)
print("--> Calling explit iterator")
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))
print(next(iterator_x))
