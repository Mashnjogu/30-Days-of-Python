# Write a function which count number of lines and number of words in a text.
# All the files are in the data the folder:
# a) Read obama_speech.txt file and count number of lines and words
# b) Read michelle_obama_speech.txt file and count number of lines and words
# c) Read donald_speech.txt file and count number of lines and words
# d) Read melina_trump_speech.txt file and count number of lines and words
import json


def no_of_lines_and_words(file):
    number_of_words = 0
    number_of_lines = 0
    with open(f'/home/dennis/PycharmProjects/30DaysOfPython/data/{file}.txt') as f:
        for line in f:
            number_of_words += len(line.split())
            number_of_lines += 1
    return f"The number of lines in {file}.txt is {number_of_lines} with a total word count of {number_of_words}"

print(no_of_lines_and_words("obama_speech"))
print(no_of_lines_and_words("michelle_obama_speech"))
print(no_of_lines_and_words("donald_speech"))
print(no_of_lines_and_words("melina_trump_speech"))

# Read the countries_data.json data file in data directory,
# create a function that finds the ten most spoken languages
# def ten_most_spoken_languages()

def most_spoken_languages(jsonFile, noOfCountries):
    with open(f'/home/dennis/PycharmProjects/30DaysOfPython/data/{jsonFile}.json', "r") as file:
        countries_list = json.load(file)
        print("The countries list is ", countries_list)
        dict = {}
        for country in countries_list:
            for language in country['languages']:
                if language in dict:
                    dict[language] += 1
                else:
                    dict[language] = 1
        print("The country dictionary is ",dict)
        country_language_list = list(dict.values())
        country_language_list.sort(reverse=True)
        top_country_list = country_language_list[:noOfCountries]
        result = []
        for x in top_country_list:
            for y in dict:
                if (x == dict[y]):
                    result.append(y)
        return result[:noOfCountries]

print(most_spoken_languages("countries_data", 10))
print(most_spoken_languages("countries_data", 5))

# Read the countries_data.json data file in data directory, create a function that creates a
# list of the ten most populated countries

def most_populated_countries(jsonFile, queryNumber):
    with open(f'/home/dennis/PycharmProjects/30DaysOfPython/data/{jsonFile}.json', "r") as file:
        countries_list = json.load(file)
        print("The countries list is ", countries_list)
        population_list = []
        for country in countries_list:
            population_list.append(country['population'])
        population_list.sort(reverse=True)
        population_list_query = population_list[:queryNumber]
        result = []
        for x in population_list_query:
            for y in countries_list:
                if(x == y['population']):
                    result.append(y['name'])
        return result[:queryNumber]

print(most_populated_countries("countries_data", 10))



