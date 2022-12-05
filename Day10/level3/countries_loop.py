import itertools
from collections import Counter

from Day10.level1.loopA import item
from data.countries import countries
from data.countries_data import countries_data


# word = 'land'
# for country in countries:
#     if word in country:
#         print(country)
#
# fruits = ['banana', 'orange', 'mango', 'lemon']
# reversed_list = []
# print("List before reversal: ", fruits)
# for value in fruits:
#     reversed_list = [value] + reversed_list
# print("List after reversal: ", reversed_list)
#
# #from the countries_data.py file
# print("The length of the countries is: ", len(countries_data))

# Find the ten most spoken languages from the data
countries_dict = {}
language_list = []
for countries_language in countries_data:
    countries_dict = countries_language
    languages = countries_dict['languages']
    # print(languages)
    for language in languages:
        language_list.append(language)

    language_set = set(language_list)

#sorting based on the frequency
frequency_languages = [
    item for items, c in Counter(language_list).most_common()
    for item in [items] * c
]

languages_sorted = []
for i in frequency_languages:
    if i not in languages_sorted:
        languages_sorted.append(i)

print(language_list)
print("The languages are: ", languages_sorted)
first_ten_languages = languages_sorted[0:10]
print("The first ten languages are: ", first_ten_languages)









