# Python Object Oriented Programming 
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes

    # TODO: create a class method
    @classmethod
    def getBookTypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    def __init__(self, title, booktype):
        self.title = title
        if(not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else: 
            self.booktype = booktype 



# TODO: access the class attribute
print("Book Type is : ", Book.getBookTypes())

# TODO: Create some book instances
b1 = Book("Title 1", "HARDCOVER")
b2 = Book("Title 2", "EBOOK")

# TODO: Use the static method to access a singleton object
