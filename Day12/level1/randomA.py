# Write a function which generates a six digit/character random_user_id.
from random import random,randint

def random_userId():
    userId = ' '.join([str(randint(0,999)).zfill(3) for _ in range(2)])
    return userId

print(random_userId())

# Modify the previous task. Declare a function named user_id_gen_by_user.
# It doesn’t take any parameters but it takes two inputs using input().
# One of the inputs is the number of characters and the second input is
# the number of IDs which are supposed to be generated
def user_id_gen_by_user():
    num_of_ids = int(input("How many Ids do you wish to generate? "))
    num_of_characters_to_be_used = int(input("How many characters do you wish to use? "))
    num_of_ids_to_be_used_in_calculation = num_of_ids - 1
    i = 0

    while i < num_of_ids_to_be_used_in_calculation:
        userId = ''.join([str(randint(0,9)) for _ in range(num_of_characters_to_be_used)])
        i = i + 1
        print(userId)

    return userId

print(user_id_gen_by_user())
