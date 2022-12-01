grade = int(input("Enter the grade of the student: "))

if 100 >= grade >= 80:
    print("A")
elif 70 <= grade <= 79:
    print("B")
elif 60 <= grade <= 69:
    print("C")
elif 50 <= grade <= 59:
    print("D")
elif 0 <= grade <= 49:
    print("F")


month = input("Enter the month you are in: ")

autumn = ("September", "October", "November")
winter = ("December", "January","February")
summer = ("June", "July","August")
spring = ("March", "April","May")

if month in autumn:
    print("Autumn")
elif month in winter:
    print("Winter")
elif month in summer:
    print("Summer")
elif month in spring:
    print("Spring")

fruits = ['banana', 'orange', 'mango', 'lemon']
my_fruit = input("Enter your favorite fruit: ")

if my_fruit in fruits:
    print("That fruit already exist in the list")
else:
    fruits.append(my_fruit)
    print(fruits)

