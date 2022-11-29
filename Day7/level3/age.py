age = [22, 19, 24, 25, 26, 24, 25, 24]

#Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age_set)
print("The list length is: ", len(age), "While the set list is: ", len(age_set))

#Explain the difference between the following data types: string, list, tuple and set

#string = a sequence of unicode characters
#list = it is ordered and modifiable
#tuple = it is ordered and immutabele
#set = it is unordered, un-indexed and immutable

# I am a teacher and I love to inspire and teach people. How many unique words have been
# used in the sentence? Use the split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
words = sentence.split()
print(words)
unique_words = set(words)
print(unique_words)