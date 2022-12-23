# Write a pattern which identifies if a string is a valid python variable
import re


# eg :- is_valid_variable('first_name') # True
# is_valid_variable('first-name') # False
# is_valid_variable('1first_name') # False
# is_valid_variable('firstname') # True

def is_valid_variable(word):
    starts_with_dogit = r'\d'
    if(re.search("-", word) or re.findall(starts_with_dogit, word)):
        return "False"
    else:
        return "True"

print(is_valid_variable("firstname"))