# Explain the difference between map, filter, and reduce.
from functools import reduce

# Map = It iterates over a list and returns the results after applying a function to every item
# in the iterable
# Filter = It filters for items that match the filtering criteria
# Reduce = It returns a single value instead of an iterable

# Explain the difference between higher order function, closure and decorator
# HighOrderFunction = This is a function that allows you perform operations on other functions
# Closure = They allow nested functions to access the outer scope of the enclosing function and returning
# the inner function
# Decorator = This is a design pattern in Python that allows a user to add new functionality to an existing
# object without modyfying its structure

# Define a call function before map, filter or reduce, see examples.
numbers1 = [2.5, 8, 2, 67]

def cube(x):
    return x ** 2

cube_map = map(cube, numbers1)
print(list(cube_map))

def is_odd(num):
    if num % 2 != 0:
        return True
    else:
        return False

cube_filter = filter(is_odd, numbers1)
print(list(cube_filter))

def add_two_nums(x,y):
    return int(x) + int(y)

cube_reduce = reduce(add_two_nums, numbers1)
print(cube_reduce)

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Use for loop to print each country in the countries list.
for country in countries:
    print(country)
# Use for to print each name in the names list.
for name in names:
    print(name)
# Use for to print each number in the numbers list.
for number in numbers1:
    print(number)
