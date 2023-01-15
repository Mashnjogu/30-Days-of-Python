# Extract all incoming email addresses as a list from the email_exchange_big.txt file.
import re
from statistics import mode

from data.stop_words import stop_words


def extract_email_address(doc_path):
    with open(doc_path) as f:
        lines = f.read()
        emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", lines))
        with open("emails.txt", "a") as t:
            for email in emails:
                t.write(str(email))
                t.write("\n")
        # pp.pprint(set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", lines)))
        return re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", lines)

# print(extract_email_address("/home/dennis/PycharmProjects/30DaysOfPython/data/email_exchange_big.txt"))

# Find the most common words in the English language.
# Call the name of your function find_most_common_words,
# it will take two parameters - a string or a file and
# a positive integer, indicating the number of words.
# Your function will return an array of tuples in descending order. Check the output

def find_most_common_words(sampleFile, occurenceOfTheWord):
    frequent_word = 0
    frequency = 0
    words_dict = {}
    words = []
    with open(f'/home/dennis/PycharmProjects/30DaysOfPython/data/{sampleFile}', "r") as file:
        for line in file:
            line_word = line.replace(',','').replace('.','').split(" ")

            for word in line_word:
                words.append(word)
        # print(words)

        for x in words:
            if(x in words_dict):
                words_dict[x] += 1
            else:
                words_dict[x] = 1

        print(words_dict)

        for key, value in words_dict.items():
            if occurenceOfTheWord == value:
                return key

        return "No word exist in such frequncy"

print(find_most_common_words("donald_speech.txt", 7))

# Use the function, find_most_frequent_words to find:
# a) The ten most frequent words used in Obama's speech'
#  b) The ten most frequent words used in Michelle's speech '
# c) The ten most frequent words used in Trump's speech '
# d) The ten most frequent words used in Melina's speech

def find_most_frequent_words(sampleFile):
    words_dict = {}
    words = []
    with open(f'/home/dennis/PycharmProjects/30DaysOfPython/data/{sampleFile}.txt') as file:
        for line in file:
            line_word = line.replace(',','').replace('.','').split(" ")

            for word in line_word:
                words.append(word)
        # print(words)
        return f"The most frequent word in {sampleFile}.txt is:- {mode(words)}"

print(find_most_frequent_words("obama_speech"))
print(find_most_frequent_words("michelle_obama_speech"))
print(find_most_frequent_words("donald_speech"))
print(find_most_frequent_words("melina_trump_speech"))

# Write a python application that checks similarity between two texts.
# It takes a file or a string as a parameter and it will evaluate the similarity of the two texts.
# For instance check the similarity between the transcripts of Michelle's and Melina's speech.
# You may need a couple of functions, function to clean the text(clean_text),
# function to remove support words(remove_support_words) and finally to check the
# similarity(check_text_similarity). List of stop words are in the data directory

def clean_text(sampleFile):
    words = []
    with open(f'/home/dennis/PycharmProjects/30DaysOfPython/data/{sampleFile}.txt') as file:
        for line in file:
            line_word = line.replace(',', '').replace('.', '').split(" ")
            for word in line_word:
                words.append(word)
        return words

def remove_support_words(sampleFile):
    final_word_list = []
    clean_txt = clean_text(sampleFile)

    for word in clean_txt:
        if(word.lower() not in stop_words):
            final_word_list.append(word)
    print(final_word_list)

def check_similarity(sampleFile1, sampleFile2):
    txt1 = remove_support_words(sampleFile1)
    txt2 = remove_support_words(sampleFile2)

print(remove_support_words("obama_speech"))

# Find the 10 most repeated words in the romeo_and_juliet.txt
def most_repeatedwords(text, number):
    wordList = []
    wordListDic = {}

    with open(f'/home/dennis/PycharmProjects/30DaysOfPython/data/{text}.txt') as f:
        for line in f:
            line_word = line.replace(',', '').replace('.', '').split(" ")
            for word in line_word:
                wordList.append(word)


        for x in wordList:
            if(x in wordListDic):
                wordListDic[x] += 1
            else:
                wordListDic[x] = 1

        wordListValues = list(wordListDic.values())
        wordListValues.sort(reverse=True)
        top_wordList = wordListValues[:number]
        result = []
        for y in top_wordList:
            for x in wordListDic:
                if(y == wordListDic[x]):
                    result.append(x)
        return result[:number]


print(most_repeatedwords("romeo_and_juliet", 10))












