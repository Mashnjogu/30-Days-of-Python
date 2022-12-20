# Use the countries_data.py (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/data/countries-data.py)
# file and follow the task
import itertools

from data.countries_data import countries_data


# Sort countries by name, by capital, by population
def sort_by_name(countries):
    countries_name = []
    for country in countries:
        countries_name.append(country["name"])
    return countries_name

def sort_by_capital(countries):
    countries_capital = []
    for country in countries:
        countries_capital.append(country["capital"])
    return countries_capital

def sort_by_population(countries):
    countries_population = []
    for country in countries:
        countries_population.append(country["population"])
    return countries_population

# Sort out the ten most spoken languages by location.

def most_spoken_languages(countries_data):
    countries_languages = []
    for country in countries_data:
        countries_languages.append(country["languages"])
    countries_languages_flattened = [country for countries in countries_languages for country in countries]

    langauage = {}
    for item in countries_languages_flattened:
        if(item in langauage):
            langauage[item] += 1
        else:
            langauage[item] = 1

    sorted_languages = sorted(langauage.items(), key= lambda i: i[1], reverse=True)
    sorted_languages_dict= dict(sorted_languages)
    top_ten_languages_available = dict(itertools.islice(sorted_languages_dict.items(), 0,10))
    return top_ten_languages_available


print(most_spoken_languages(countries_data))

# Sort out the ten most populated countries.
def most_populated(countries):
    population_dict = {}
    country_name = []
    country_population = []
    for country in countries:
        country_name.append(country["name"])
    for country1 in countries:
        country_population.append(country1["population"])

    for key in country_name:
        for value in country_population:
            population_dict[key] = value
            country_population.remove(value)
            break

    most_populated_countries = dict(sorted(population_dict.items(),key = lambda i:i[1], reverse= True))
    topten_most_populated = dict(itertools.islice(most_populated_countries.items(),0,10))
    return topten_most_populated

print(most_populated(countries_data))