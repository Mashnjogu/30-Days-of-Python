# Read this url and find the 10 most frequent words.
# romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
import statistics

import requests

# url = "http://www.gutenberg.org/files/1112/1112.txt"
# response = requests.get(url)
# text = response.text
#
# def most_repeatedwords(text, number):
#     word_dict = {}
#
#     for word in text.split():
#         if word.isalnum():
#             if word_dict.get(word):
#                 word_dict[word] += 1
#             else:
#                 word_dict[word] = 1
#     sorted_words = sorted(word_dict.items(), key= lambda x : x[1],  reverse= True)
#     return sorted_words[:number]
#
# print(most_repeatedwords(text, 10))

# Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :
# the min, max, mean, median, standard deviation of cats' weight in metric units.
# the min, max, mean, median, standard deviation of cats' lifespan in years.
# Create a frequency table of country and breed of cats
url2 = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(url2)
cats_data = response.json()




def weight_metrics(cats):
    for cat in cats:
        arr = []

        for num in cat["weight"]["metric"]:
            if num.isdigit():
                arr.append(int(num))
                total_weight = sum(arr)
        min_weight = min(total_weight)
        max_weight = max(total_weight)
        std_dev = statistics.stdev(total_weight)
        return f"The minimum weight is: {min_weight} , maximum weight is: {max_weight} and standard deviation is: {std_dev}"



print(weight_metrics(cats_data))

