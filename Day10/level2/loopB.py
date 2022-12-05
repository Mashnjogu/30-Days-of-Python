#Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for value in range(0, 101):
    sum = sum + value

print(sum)

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0
for value in range(0, 101):
    if(value % 2 == 0):
        sum_even = sum_even + value
    elif(value % 2 != 0):
        sum_odd = sum_odd + value

print("The value of even numbers is: ", sum_even)
print("The value of odd numbers is: ", sum_odd)
