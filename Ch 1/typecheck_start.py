# Python Object Oriented Programming by Joe Marini course example
# Checking class types and instances


class Book:
    def __init__(self, title):
        self.title = title


class Newspaper:
    def __init__(self, name):
        self.name = name


# Create some instances of the classes
b1 = Book("The Catcher In The Rye")
b2 = Book("The Grapes of Wrath")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
# print(type(b1))
# print(type(n1))

# TODO: compare two types together
# def compareDataType(self): 
#     if (type(b1) == type(b2)):
#         print("The same data type")
#     else:
#         print("not the same data type")
# print(type(b1) == type(b2))
# print(type(n1) == type(b1))

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, Book))
print(isinstance(n1, object))