# Python - Inheritance

This repository contains code examples that illustrate essential concepts of inheritance in Python programming. Topics covered include:

- Superclass, baseclass, and subclasses
- Utilizing parent classes' attributes and methods
- Overwriting parent classes' methods

## Project Structure

- **main_files:** Contains main programs showcasing examples of how to use functions
- **tests:** Holds tests and edge cases for checking

## File Descriptions

Files are numbered and demonstrate the following concepts:

0. Function that returns a list of attributes and methods of an object
1. Class that inherits from list and prints a sorted list
2. Function using `type()` - same object
3. Function using `isinstance()` - same class inherited from
4. Function using `issubclass()` - only subclass of
5. Empty class `BaseGeometry` (foundation for subsequent examples)
6. Add empty `area()` method to `BaseGeometry`
7. Add `integer_validator()` method to `BaseGeometry`
8. Class `Rectangle` that inherits from `BaseGeometry`; initializes private width and height
9. Implement `__str__` to print `Rectangle`
10. Class `Square` that inherits from `Rectangle`; initialize size and use area
11. Implement `area()` and print for `Square`
100. Class `MyInt` that inherits from `int`; inverts `==` and `!=` operations
101. Set attribute to object if possible

## Environment

- **Language:** Python 3.9.5
- **OS:** Ubuntu 20.04 LTS
- **Compiler:** python3
- **Style Guidelines:**
  - [PEP 8 (version 1.7)](https://www.python.org/dev/peps/pep-0008/)
  - [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

## Author

Hassan ahmed