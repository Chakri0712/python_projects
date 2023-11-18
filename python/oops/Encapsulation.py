"""The process of binding data and corresponding methods (behavior) together into a single unit is called
encapsulation in Python.

In other words, encapsulation is a programming technique that binds the class members (variables and methods)
together and prevents them from being accessed by other classes. It is one of the concepts of OOPS in Python.

Encapsulation is a way to ensure security. It hides the data from the access of outsiders. An organization can
protect its object/information against unwanted access by clients or any unauthorized person by encapsulating it.

We mainly use encapsulation for Data Hiding. We do so by defining getter and setter methods for our classes. If
anyone wants some data, they can only get it by calling the getter method. And, if they want to set some value to the
data, they must use the setter method for that, otherwise, they won't be able to do the same."""


class Library:
    def __init__(self, book_id, book_name):
        self.book_id = book_id
        self.book_name = book_name

    def set_book_name(self, new_book_name):
        # Setter method to set the book name
        self.book_name = new_book_name

    def get_book_name(self):
        # Getter method to get the book name
        return self.book_name


if __name__ == "__main__":
    # Creating an instance of the Library class
    book = Library(101, "The Witchers")

    # Using the getter method to get the initial book name
    print(f"The name of the book is {book.get_book_name()}")

    # Using the setter method to set a new book name
    book.set_book_name("The Witchers Returns")

    # Using the getter method to get the updated book name
    print(f"The updated name of the book is {book.get_book_name()}")

"""

In Python, it's a convention to use a single leading underscore for protected attributes and a double leading 
underscore for private attributes. Also, it's a good practice to use getter methods to access private attributes. 
Here's the refactored code:"""


class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name  # making employee name public
        self._emp_id = employee_id  # making employee ID protected
        self.__salary = salary  # making salary private

    def get_salary(self):  # getter method for accessing private salary attribute
        return self.__salary


# Creating an instance of the Employee class
employee1 = Employee("John Gates", 110514, "$1500")

# Accessing public and protected attributes directly
print(f"The Employee's name is {employee1.name}")
print(f"The Employee's ID is {employee1._emp_id}")

# Accessing private attribute using the getter method
print(f"The Employee's salary is {employee1.get_salary()}")
