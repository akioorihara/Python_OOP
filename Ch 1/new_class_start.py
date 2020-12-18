# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARD", "PAPER", "E")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None 

    # TODO: create a class method
    @classmethod
    def getBookTypes(self):
        return self.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getBookList():
        if(Book.__booklist is None):
            Book.__booklist = []
        return Book.__booklist
             
    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid input")
        else:
            self.booktype = booktype

# TODO: access the class attribute
print("Book Types are : ", Book.getBookTypes())
#print(Book.BOOK_TYPES)

# TODO: Create some book instances
b1 = Book("Title 1", "E")
b2 = Book("Title 2", "HARD")

# TODO: Use the static method to access a singleton object
theBooks = Book.getBookList()
print("Our Book list is : ", theBooks)
theBooks.append(b1)
theBooks.append(b2)
print("Out Book list is now : ", theBooks)