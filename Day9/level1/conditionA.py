age = int(input("Enter your age: "))

if age > 18:
    print("You are old enough to drive")
else:
    print(f"You need {18 - age} years to learn how to drive")

my_age = int(input("Enter my age: "))
your_age = int(input("Enter your age: "))

if your_age > my_age:
    print(f"Your are {your_age - my_age} years older than me")
elif my_age > your_age:
    print("I am {my_age - your_age} years older than you")
else:
    print("We both are in the same age")

a = int(input("Enter number one"))
b = int(input("Enter number two"))

if a > b:
    print(a, " is greater than ", b)
else:
    print(b, " is less than ", a)