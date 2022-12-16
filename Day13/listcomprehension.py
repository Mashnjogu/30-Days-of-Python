# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_numbers = [i for i in numbers if i < 0 or i == 0]
print(negative_numbers)

# Flatten the following list of lists of lists to a one dimensional list :
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flat_list = [item for items in list_of_lists for item in items]
flat_list2 = [item for items in flat_list for item in items]
print(flat_list2)

# Using list comprehension create the following list of tuples:
list_tuple = [(0, 1, 0, 0, 0, 0, 0),
(1, 1, 1, 1, 1, 1, 1),
(2, 1, 2, 4, 8, 16, 32),
(3, 1, 3, 9, 27, 81, 243),
(4, 1, 4, 16, 64, 256, 1024),
(5, 1, 5, 25, 125, 625, 3125),
(6, 1, 6, 36, 216, 1296, 7776),
(7, 1, 7, 49, 343, 2401, 16807),
(8, 1, 8, 64, 512, 4096, 32768),
(9, 1, 9, 81, 729, 6561, 59049),
(10, 1, 10, 100, 1000, 10000, 100000)]

tuple_list = [i for item in list_tuple for i in item]
print(tuple_list)

# Flatten the following list to a new list:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
tuple_countries = [i for item in countries for i in item]
print(tuple_countries)
list_countries = [list(element) for element in tuple_countries]
print(list_countries)

# Change the following list to a list of dictionaries:
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
key = ["country", "city"]
x = [i for items in countries for i in items]
print("########")
print(x)
list_country_city = []
for j in x:
    dict = {}
    dict["country"] = j[0]
    dict["city"] = j[1]
    list_country_city.append(dict)
print(list_country_city)

# Change the following list of lists to a list of concatenated strings:
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
list_names = [x for items in names for x in items]
print("Concatenated Strings")
print(list_names)
list_names1 = [list(element) for element in list_names]
print(list_names1)
list_names2 = [item for items in list_names1 for item in items]
print(list_names2)


# Write a lambda function which can solve a slope or y-intercept of linear functions.
x = lambda x1,x2,y1,y2: (y2-y1)/(x2-x1)
print(x)


