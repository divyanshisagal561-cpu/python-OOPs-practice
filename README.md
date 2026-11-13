# 🐍 Python OOP Practice

A beginner-friendly Python project focused on learning and practicing the fundamentals of **Object-Oriented Programming (OOP)** through practical coding exercises.

This repository contains multiple examples covering classes, objects, constructors, methods, instance variables, class variables, inheritance, method overriding, and a small product-management mini project.

---

## 📌 About the Project

The purpose of this project is to build a strong foundation in **Python Object-Oriented Programming** by implementing concepts through simple, real-world examples.

The exercises gradually progress from basic class creation to inheritance and a small practical project.

---

## 🎯 Learning Objectives

Through this project, you will practice:

* Creating classes and objects
* Using constructors with `__init__()`
* Understanding the `self` keyword
* Creating and calling class methods
* Working with multiple objects
* Performing calculations using methods
* Understanding instance variables
* Understanding class variables
* Implementing inheritance
* Implementing method overriding
* Building a small OOP-based mini project

---

## 📚 Concepts Covered

### 1. Class & Object 👤

Created a `Student` class with:

* Name
* Age
* Course

Three different student objects are created and their details are displayed.

---

### 2. Constructors 🚗

Created a `Car` class using a constructor that accepts:

* Brand
* Model
* Price

Two car objects are created and their information is displayed.

---

### 3. Methods in a Class 📐

Created a `Rectangle` class containing:

* Length
* Width

An `area()` method calculates and returns the area of the rectangle.

**Formula:**

```text
Area = Length × Width
```

---

### 4. Using `self` 👤

Created a `Person` class containing:

* Name
* City

The `introduce()` method uses `self` to access object attributes and display a person's introduction.

---

### 5. Multiple Objects 👨‍💼

Created an `Employee` class containing:

* Name
* Salary
* Department

Three employee objects are created to demonstrate how a single class can be used to create multiple independent objects.

---

### 6. Methods with Calculations 🏦

Created a `BankAccount` class containing:

* Account holder
* Balance

Methods include:

* `deposit()` — adds money to the balance
* `withdraw()` — subtracts money from the balance
* `check_balance()` — displays the current balance

This exercise demonstrates how methods can modify object data.

---

### 7. Class Variable vs Instance Variable 🏫

Demonstrates the difference between:

**Instance variable**

```python
self.name
```

Each object can have a different value.

**Class variable**

```python
school = "ABC School"
```

The value is shared by objects of the class.

---

### 8. Inheritance & Method Overriding 🐶

Created:

* `Animal` → Parent class
* `Dog` → Child class

The `Dog` class inherits from `Animal` and overrides the `sound()` method.

This demonstrates two important OOP concepts:

* Inheritance
* Method overriding

---

## ⭐ Mini Project — Product Management

The project also includes a small **Product** class.

### Product Attributes

* Name
* Price
* Quantity

### Methods

#### `display_product()`

Displays the product information.

#### `total_price()`

Calculates the total price using:

```text
Total Price = Price × Quantity
```

Three products are created and their total prices are calculated.

---

## 🗂️ Project Structure

```text
Python-OOP-Practice/
│
├── oop.py
├── screenshots.png
└── README.md
```

---


## 📖 OOP Concepts Practiced

| Concept                    | Implemented |
| -------------------------- | :---------: |
| Classes                    |      ✅      |
| Objects                    |      ✅      |
| Constructors               |      ✅      |
| `self` keyword             |      ✅      |
| Instance Variables         |      ✅      |
| Class Variables            |      ✅      |
| Methods                    |      ✅      |
| Multiple Objects           |      ✅      |
| Calculations using Methods |      ✅      |
| Inheritance                |      ✅      |
| Method Overriding          |      ✅      |

---

## 👩‍💻 Author

**Divyanshi Sagar**

Learning Python, SQL, Data Analytics, and other technology skills through hands-on projects.

---

## ⭐ Support

If you found this project useful for learning Python OOP, consider giving the repository a ⭐ on GitHub.

**Happy Coding! 🐍💻**
