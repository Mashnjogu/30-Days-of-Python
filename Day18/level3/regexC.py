# Clean the following text. After cleaning, count three most frequent words in the string.
import re

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

clean_sentence1 = re.sub("%",'', sentence)
clean_sentence2 = re.sub("@",'',clean_sentence1)
clean_sentence3 = re.sub("&",'', clean_sentence2)
clean_sentence4 = re.sub(";",'',clean_sentence3)
clean_sentence5 = re.sub("#",'',clean_sentence4)
dollar_sign = re.match("$", clean_sentence5)
clean_sentence6 = re.sub("$",'',clean_sentence5)
print(clean_sentence6)
