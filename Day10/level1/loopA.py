numbers = list(range(0,11))
print(numbers)

count = 11
while(count > 0):
    count = count - 1
    print(count)


# Number of rows
rows = 5

# Outer loop to handle the rows
for i in range(rows):

    # Inner loop to handle the columns
    for j in range(i + 1):
        # Printing the pattern
        print("*", end=' ')

    # Next Line
    print()


side = 8

for i in range(side):
    for i in range(side):
        print("#", end= ' ')
    print()


for i in range(11):
    print(i ,"*", i , " = ", i * i)

my_list = ['Python', 'Numpy','Pandas','Django', 'Flask']

for item in my_list:
    print(item)

#even numbers
for number in range(0, 101):
    if number % 2 == 0:
        print(number)

#odd numbers
for number in range(0, 101):
    if number % 2 != 0:
        print(number)