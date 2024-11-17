# OOPS Concepts in Python

## Classes and Objects
* Class: A blueprint for creating objects (an object is an instance of a class).

```python
# Creating a class
class Student:
    name = "Thanmai Sai"

# Creating an object
s1 = Student()
print(s1.name)  # Output: Thanmai Sai
```
* Object: An instance created from a class. Without a class, an object cannot exist.

## `__init__` Function (Constructor)

* A special method that runs as soon as an object of the class is instantiated.

* Used to initialize object properties.

```python
# Creating a class with a constructor
class Student:
    def __init__(self, name):
        self.name = name  # Initializing instance variable

# Creating an object
s1 = Student("Thanmai Sai")
print(s1.name)  # Output: Thanmai Sai

```
* The self parameter refers to the current instance of the class and is used to access variables that belong to the class.

Example with Multiple Attributes
```python

class Student:
    college_name = "ABC College"  # Class attribute
    name = "anonymous"            # Class attribute

    def __init__(self, name, marks):
        self.name = name          # Instance attribute (overrides class attribute)
        self.marks = marks
        print("Adding new student to Database...")

s1 = Student("Karan", 97)
print(s1.name)  # Output: Karan

```

* Constructor Types
    - Default Constructor: A constructor with no parameters or one that initializes default values.
    - Parameterized Constructor: A constructor that accepts parameters.

    ```python
    # Default Constructor
    class DefaultExample:
        def __init__(self):
            self.message = "This is a default constructor"

        def display(self):
            print(self.message)

    # Creating an object of DefaultExample
    obj1 = DefaultExample()
    obj1.display()  # Output: This is a default constructor


    # Parameterized Constructor
    class ParameterizedExample:
        def __init__(self, message):
            self.message = message  # Initializing with a parameter

        def display(self):
            print(self.message)

    # Creating an object of ParameterizedExample
    obj2 = ParameterizedExample("This is a parameterized constructor")
    obj2.display()  # Output: This is a parameterized constructor
    ```
    Explanation:
    
    * The default constructor doesn't take any arguments (other than self), while the parameterized constructor accepts arguments and can initialize object properties accordingly.








# Static methods
* A method that does not access or modify class or instance data (no self parameter).
* Works at the class level and can be called on the class itself.

```python
class Student:
    @staticmethod  # Decorator
    def college():
        print("ABC College")

Student.college()  # Output: ABC College
```

* Decorators: Used to extend the behavior of a function or method without modifying it permanently.

# Abstraction
* Hides implementation details and shows only the essential features of the object.

```python
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

car1 = Car()
car1.start()  # Output: Car started
```

# Encasplation
* Bundling data (variables) and methods (functions) into a single unit (object).
* Example: A capsule that contains data and related functions together.


```python
class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account = acc
    
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())

    def get_balance(self):
        return self.balance

# Example usage
acc1 = Account(1000, 12345)
acc1.debit(200)  # Rs. 200 was debited
```
