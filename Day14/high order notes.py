def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def high_order_function(type):
    if type == 'square':
        return square
    elif type == 'cube':
        return cube

result = high_order_function('cube')
print(result(3))

#Python Closure
# Python allows a nested function to access the outer scope of the enclosing function.
# This is is known as a Closure. Let us have a look at how closures work in Python.
# In Python, closure is created by nesting a function inside another encapsulating
# function and then returning the inner function
def add_ten():
    ten = 10
    def add_num(num):
        return num + ten
    return add_num

close_result = add_ten()
print(close_result(5))

# A decorator is a design pattern in Python that allows a user to add new functionality to an existing
# object without modifying its structure.
# Decorators are usually called before the definition of a function you want to decorate.
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase
    return wrapper

def lowecase_decorator(function):
    def wrapper():
        func = function()
        make_lowercase = func.lower()
        return make_lowercase
    return wrapper

@lowecase_decorator
def greeting():
    return 'Day 14 of Python'

print(greeting())
@uppercase_decorator
def greeting():
    return 'Welcome to Python'

print(greeting())

# Built-in high order
numbers = [1,3,4,7,8,9]
def square(x):
    return x ** 2

numbers_squared = map(square, numbers)
print(list(numbers_squared))
