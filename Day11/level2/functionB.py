import statistics


def even_and_odd(num):
    even_total = 0
    odd_total = 0

    for number in range(num + 1):
        if(number % 2 == 0):
            even_total += 1
        elif(number % 2 != 0):
            odd_total += 1
    return f"The number of odd are {odd_total} and the number of even are {even_total}"

print(even_and_odd(100))

def factorial(num):
    if num < 0:
        return 0
    elif num == 0 or num == 1:
        return 1
    else:
        factorial = 1
        while(num > 1):
            factorial *= num
            num -= 1
    return factorial

print(factorial(5))

def is_empty(param):
    if len(param) == 0:
        print("Empty params")
    else:
        print("Not empty")

print(is_empty("jjk"))

def calculate_mean(*params):
    no_of_items = len(params)
    total = 0
    for num in params:
        total = total + num
    mean = total / no_of_items
    return mean

def calculate_median(*params):
    length = len(params)
    index = length // 2

    if length % 2:
        return sorted(params)[index]
    else:
        return sum(sorted(params)[index - 1: index + 1])/2

def calculate_mode(*params):
    return statistics.mode(params)

def calculate_range(*params):
    min_val = min(params)
    max_val = max(params)

    return (min_val, max_val)

print("#")
print(calculate_mean(7,8,9,3,2))
print(calculate_mode(7,8,9,3,2))
print(calculate_median(7,8,9,3,2))
print(calculate_range(7,8,9,3,2))