# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages 
        self.price = price 
        # TODO: add properties

    # TODO: create instance methods
    def getPrice(self):
        return self.price 

# TODO: create some book instances
b1 = Book("War and Peace", "Akio Orihara", 99, 2.00)
b2 = Book("The Catcher in the Rye", "Ashley", 11, 11.0)

# TODO: print the price of book1
print("The price is :", b1.price)


# TODO: try setting the discount


# TODO: properties with double underscores are hidden by the interpreter
