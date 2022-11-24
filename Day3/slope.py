# Calculate the slope, x-intercept and y-intercept of y = 2x -2

def slope(x1, y1, x2, y2):
    s = (y2 - y1)/ (x2 - x1)
    return s

print(slope(45, 78, 50, 40))


# Calculate the value of y (y = x^2 + 6x + 9).
# Try to use different x values and figure out at what x value y is going to be 0.

x = int(input("Enter the value of x:"))
y = x ** 2 + (6 * x) + 9
print('When x is ', x, 'the value of y is ', y)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement.
# Use and operator to check if 'on' is found in both 'python' and 'dragon'
pythonLength = len("python")
dragonLength = len("dragon")
if(pythonLength == dragonLength):
    print("The lengths are the same")
elif(pythonLength > dragonLength):
    print("Python has more characters than Dragon")
else:
    print("Dragon has more characters than Python")
#
python = "Python"
dragon = "Dragon"

if(python.__contains__("on") and dragon.__contains__("on")):
    print("They both have on")

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
sentence = "I hope this course is not full of jargon"
if(sentence.__contains__("jargon")):
    print("It contains jargon")


