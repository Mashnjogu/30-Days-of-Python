# Write a function called is_prime, which checks if a number is prime.
from data.countries_data import countries_data

def is_prime(number):
    for i in range(2, number):
        if(number % i ) == 0:

            print("This is not a prime number")
            break
        else:

            print("This is a prime number")

print(is_prime(7))

# Write a functions which checks if all items are unique in the list.
items = ["Messi", "Dennis", "Aguero", "Ronaldo", "Messi"]
def is_unique(items):
    for item in items:
        if items.count(item) > 1:
            return  True
        return False

if is_unique(items):
    print("There are duplicate values")
else:
    print("No duplicate values")

# Write a function which checks if all the items of the list are of the same data type.
def check_data_type(listItem):
    i = 0
    while i < len(listItem) - 1:
        if (type(listItem[i]) != type(listItem[i + 1])):
            return False
        i += 1
    return True

print(check_data_type([9,5,6,2,4,9,"Dennis", "Biro"]))

# Create a function called the most_spoken_languages in the world.
# It should return 10 or 20 most spoken languages in the world in descending order
def most_spoken_langauges(country_data):
    dict = {}
    for country in country_data:
        for language in country['languages']:
            if language in dict:
                dict[language] += 1
            else:
                dict[language] = 1
    print(dict)
    country_language_list = list(dict.values())
    country_language_list.sort(reverse= True)
    top_ten_country_language_list = country_language_list[:10]
    result = []
    for i in top_ten_country_language_list:
        for z in dict:
            if (i == dict[z]):
                result.append(z)
    print("Most popular language results")
    print(result[:10])
    return result[:10]

most_spoken_langauges(country_data = countries_data)

# Create a function called the most_populated_countries.
# It should return 10 or 20 most populated countries in descending order.
def most_populated_countries(country_data):
    population_list = []
    for i in country_data:
        population_list.append(i["population"])
    population_list.sort(reverse= True)
    top_ten_population_list = population_list[:10]
    result = []
    for i in top_ten_population_list:
        for j in country_data:
            if(i == j["population"]):
                result.append(j["name"])
    print("# Population Results")
    print(result)
    return result

most_populated_countries(countries_data)


