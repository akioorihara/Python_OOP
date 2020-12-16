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
        self.__secret = "This is a secret key!"
        # TODO: add properties

    # TODO: create instance methods
    def getPrice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price 

    def getDiscount(self, amount):
        self._discount = amount 
 
# TODO: create some book instances
b1 = Book("War and Peace", "Akio Orihara", 99, 2.00)
b2 = Book("The Catcher in the Rye", "Ashley", 11, 29.95)

# TODO: print the price of book1
#print("The price is :", b1.price)
#print(b1.getPrice())
#print(b2.getPrice())

# TODO: try setting the discount
print(b2.getPrice())
b2.getDiscount(0.25)
print(b2.getPrice())

# TODO: properties with double underscores are hidden by the interpreter
print(b1._Book__secret)