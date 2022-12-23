# What is the most frequent word in the following paragraph?
from statistics import mode
import re

paragraph = "I love teaching. If you do not love teaching what else can you love." \
            " I love Python if you do not love something which can give you all the capabilities to develop" \
            " an application what else can you love."

all_words = [word for i in paragraph for word in paragraph.split()]
print(all_words)

# getting the frequency
freq = mode(all_words)
print("The most frequent word is ", str(freq))

text = "The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in" \
       " the negative direction, 0 at origin, 4 and 8 in the positive direction. " \
       "Extract these numbers from this whole text and find the distance between the two " \
       "furthest particles."
all_numbers = r'-?\d+'
matches = re.findall(all_numbers, text)
print(matches)
neg_num = []
for num in matches:
    if int(num) < 0:
        neg_num.append(num)
print("The negative numbers are:",neg_num)

furthest_negative_number = max(neg_num)
furthest_positive_number = max(matches)
diff = int(furthest_negative_number) - int(furthest_positive_number)
print("The difference between the two furthest points is ", diff)