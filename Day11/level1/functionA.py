
def addNumber(a,b):
    total = a + b
    return total

print(addNumber(3,6))

# Write a function that calculates area_of_circle.
def areaOfCircle(radius):
    pie = 3.142
    area = pie * radius * radius
    return area

print(areaOfCircle(14))

def add_all_nums(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(add_all_nums(7,8,3,4))

def convert_celcius_to_fahrenheit(celcius):
    farenheight = (celcius * 9/5) + 32
    return farenheight

print(convert_celcius_to_fahrenheit(33))

import math
import sys

autumn = ["September", "October", "November"]
winter = ["December", "January", "February"]
spring = ["March", "April", "May"]

def check_season(month):
    if month in autumn:
        print("It is in Autumn")
    elif month in winter:
        print("It is in Winter")
    elif month in spring:
        print("It is in Spring")

print(check_season("May"))

#calculate the slope of a linear equation
def calculate_slope(x1, y1, x2, y2):
    if (x2 - x1 != 0):
        return (float)(y2 - y1) / (x2 - x1)
    return sys.maxint

print(calculate_slope(3,4,9,2))

def solve_quadratic_eqn(a, b, c):
    # calculating discriminant using formula
    dis = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(dis))

    # checking condition for discriminant
    if dis > 0:
        print(" real and different roots ")
        print((-b + sqrt_val) / (2 * a))
        print((-b - sqrt_val) / (2 * a))

    elif dis == 0:
        print(" real and same roots")
        print(-b / (2 * a))

        # when discriminant is less than 0
    else:
        print("Complex Roots")
        print(- b / (2 * a), " + i", sqrt_val)
        print(- b / (2 * a), " - i", sqrt_val)

print(solve_quadratic_eqn(2, 6, 9))

# Declare a function named print_list.
# It takes a list as a parameter and it prints out each element of the list.
def print_list(*items):
    for item in items:
        print(item)

print(print_list("Shoe", "Car", "Book", "Pen", "Ink"))

# Declare a function named reverse_list.
# It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(*items):
    original_list = []
    reverse_list = []
    for item in items:
        original_list.append(item)
    print("The original list is: ",original_list)

    for value in original_list:
        reverse_list = [value] + reverse_list
    print("The reversed list is: ", reverse_list)

print(reverse_list("Messi", "Neymar", "Ronaldo", "Sancho"))

# Declare a function named capitalize_list_items.
# It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(*items):
    itemList = []
    for item in items:
        itemList.append(item)

    itemsUpper = []
    for value in itemList:
        itemsUpper.append(value.upper())
    print(itemsUpper)

print(capitalize_list_items("Dennis", "Jose", "Mash", 'Fei'))


def add_item(*foodstaff, accompanyment):
    foodstaffList = []
    flatlist = []
    for food in foodstaff:
        foodstaffList.append(food)

    for element in foodstaffList:
        if type(element) is list:
            for item in element:
                flatlist.append(item)
        else:
            flatlist.append(item)

    flatlist.append(accompanyment)
    # foodstaffList.append(accompanyment)
    print(flatlist)

foodstaffs = ["Cabbage", "Carrot", "Tomato"]
print(add_item(foodstaffs, accompanyment='Juice'))

# Declare a function named sum_of_numbers.
# It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum = sum + number
    return sum
print(sum_of_numbers(2,3,5,6))

# Declare a function named sum_of_odds.
# It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(*numbers):
    sum = 0
    for number in numbers:
        if (number % 2 != 0):
            sum = sum + number
    return sum

# Declare a function named sum_of_even.
# It takes a number parameter and it adds all the even numbers in that - range
def sum_of_even(*numbers):
    sum = 0
    for number in numbers:
        if (number % 2 == 0):
            sum = sum + number
    return sum

print(sum_of_odds(2,3,4,5,6,7))
print(sum_of_even(2,3,4,5,6,7))




