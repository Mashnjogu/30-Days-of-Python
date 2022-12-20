from functools import reduce

from data.countries import countries

countries1 = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']

# Use map to create a new list by changing each country to uppercase in the countries list
def change_to_upper(country):
    return country.upper()

countries_upper = map(change_to_upper, countries1)
print(list(countries_upper))

# Use map to create a new list by changing each number to its square in the numbers list
def square(num):
    return num ** 2

num_square = map(square, numbers)
print("Original", numbers)
print("Squared", list(num_square))

# Use map to change each name to uppercase in the names list
names_upper = map(change_to_upper, names)
print(list(names_upper))

# Use filter to filter out countries containing 'land'.
def contains_land(country):
    if 'land' in country:
        return True
    else:
        return False

countries_with_land = filter(contains_land, countries1)
print(list(countries_with_land))

# Use filter to filter out countries having exactly six characters.
def country_with_six_characters(country):
    if (len(country) == 6):
        return True
    else:
        return False

country_6 = filter(country_with_six_characters, countries1)
print(list(country_6))

# Use filter to filter out countries containing six letters and more in the country list.
def six_or_more(country):
    if(len(country) >= 6):
        return True
    else:
        return False

country_6_or_more = filter(six_or_more, countries1)
print(list(country_6_or_more))

# Use filter to filter out countries starting with an 'E'
def country_starting_with_an_E(country):
    if(country.startswith('E')):
        return True
    else:
        return False

country_with_E = filter(country_starting_with_an_E, countries1)
print(list(country_with_E))

# Declare a function called get_string_lists which takes a list
# as a parameter and then returns a list containing only string items.
def get_string_list(list):
    string_list = []
    for item in list:
        if type(item) == str:
            string_list.append(item)
    return string_list

mixed_list = ["Germany", "Argentina", 8, 90, "Dennis"]
list_with_strings = get_string_list(mixed_list)
print(list_with_strings)

# Use reduce to concatenate all the countries and to produce this sentence:
# Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def concatenate_countries(x,y):
    return f"{x}, {y}"

all_countries = reduce(concatenate_countries, countries1)
print(all_countries, "are north European countries")

# Create a function returning a dictionary, where keys stand for starting
#     letters of countries and values are the number
# of country names starting with that letter.

def country_dict_initial(countries):
    country_dict = {}
    for country in countries:
        if(country[0] in country_dict):
            country_dict[country[0]] += 1
        else:
            country_dict[country[0]] = 1
    return country_dict

print(country_dict_initial(countries))

# Declare a get_first_ten_countries function - it returns a list of first ten countries
# from the countries.js list in the data folder.
def get_first_ten_countries(countries):
    return countries[:10]

print(get_first_ten_countries(countries))

# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.
def get_last_ten_countries(countries):
    return countries[-10:]

print(get_last_ten_countries(countries))




