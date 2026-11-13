# 1. Class & Object
# Create a Student class with the attributes:
# name
# age
# course
# Create 3 objects and display their details

class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def student_details(self):
        print("Name:",self.name)
        print("Age:", self.age)
        print("Course:", self.course)    

student1 = Student("Rohit kumar", 17, "Maths")
student2 = Student("Purv Singh", 16, "English")
student3 = Student("Uday Lal", 17, "Science")

student1.student_details()
student2.student_details()
student3.student_details()

# 2. Create a class Car with a constructor that takes:

# brand
# model
# price

# Create two car objects and print their details.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def car_details(self):
        print("Car Brand:",self.brand)
        print("Car Model:",self.model)
        print("Car Price:",self.price)

    
car1 = Car("BMW", "p001", 2000000)
car2 = Car("Audi", "Qm018", 5600000)

car1.car_details()
car2.car_details()

# 3. Methods in a Class
# Create a class Rectangle with:

# length
# width

# Create a method area() that returns the area of the rectangle.


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

r1 = Rectangle(10, 2)

print("The area of rectangle:",r1.area())

# 4. Using self
# Create a class Person with:

# name
# city

# Create a method introduce() that prints:

# My name is Divyanshi and I live in Delhi.

# Use self to access the attributes.

class Person:
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def introduce(self):
        print(f"My name is {self.name} and I live in {self.city}.")

p1 = Person("Divyanshi", "Delhi")            

p1.introduce()

print(p1.name)
print(p1.city)

# 5. Multiple Objects
# Create a class Employee with:

# name
# salary
# department

# Create 3 different employee objects and print their information.

class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def employee_info(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Department:",self.department)

e1 = Employee("Shri Ram", 95000, "IT")
e2 = Employee("Rohit Singh", 75000, "Medical")
e3 = Employee("Deepika Radu", 32000, "Management")        

e1.employee_info()
e2.employee_info()
e3.employee_info()

# 6. Method with Calculation
# Create a class BankAccount with:

# account_holder
# balance

# Create two methods:

# deposit(amount) → adds money
# withdraw(amount) → subtracts money

# Create an object and perform both operations. 

class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited amount:", amount)

    def withdraw(self, amount):
        self.balance = self.balance - amount
        print("Withdraw amount:", amount)  

    def check_balance(self):
        print("Current balance:", self.balance)    
        
ah = BankAccount("Divya Singh", 100)

ah.deposit(100)
ah.withdraw(50)

ah.check_balance()

# 7. Class Variable vs Instance Variable
# Create a class Student with:

# instance variable: name   # Instance variable → Different for every object.
# class variable: school = "ABC School"    # Class variable → Shared by all objects.

# Create two student objects and print their names and school.

class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name

stu1 = Student("Rohit")
stu2 = Student("Sharma")

print(stu1.name)   # Instance variable
print(stu1.school)    # Class variable 

print(stu2.name)    # Instance variable
print(stu2.school)     # Class variable 

# 8. Simple Inheritance
# Create a parent class Animal with a method:

# sound()

# Create a child class Dog that inherits from Animal and overrides sound() to print:

# Dog barks

class Animal:
    def sound(self):
        print("Animal make a sound!")

class Dog(Animal):
    def sound(self):
        print("Dog bark")

dog1 = Dog()

dog1.sound()

# MINI PROJECT ⭐

# Create a class Product with:

# name
# price
# quantity

# Create methods:

# display_product() → displays product details
# total_price() → returns price × quantity

# Create 3 products and display their total prices.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print("Product name:", self.name)
        print("Product price:", self.price)
        print("Product quantity:", self.quantity)

    def total_price(self): 
        return self.price * self.quantity 

product_1 = Product("Amul Milk", 300, 2)
product_2 = Product("Kit kat", 100, 4)          
product_3 = Product("Pen", 2, 30)

product_1.display_product()
print("Total price:",product_1.total_price())

product_2.display_product()
print("Total price:",product_2.total_price())

product_3.display_product()
print("Total price:",product_3.total_price())
















































































































































































































