#Split the string 'Coding For All' using space as the separator (split())
sentence = "Coding For All"
print('Character at index 0 is:', sentence[0])
lastIndex = len(sentence) - 1
print('The last character is:', sentence[lastIndex])
print("The character at index 10 is:", sentence[10])
#function to create acronym
def acronym(str):
    output = str[0]
    for i in range(1, len(str)):
        if str[i - 1] == ' ':
            #add letter to the next space
            output += str[i]

    #uppercase output
    output = output.upper()
    return output
print(acronym(sentence))

# Use index to determine the position of the first occurrence of C in Coding For All.
print(sentence.find('C'))
# Use index to determine the position of the first occurrence of F in Coding For All.
print(sentence.find('F'))
# Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(sentence.rfind('l'))


# print(sentence.split())"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

sentence2 = 'You cannot end a sentence with because because because is a conjunction'
print(sentence2.find('because'))
print('last occurence of because is:', sentence2.rfind("because"))
sentence3 = sentence2[31:47]
print('when becasue is sliced out', sentence3)
print(sentence.startswith('Coding'))
print(sentence.endswith('coding'))
sentence4 = ' Coding For All '
print("When trails are removed: ", sentence4.strip())

# Which one of the following variables return True when we use the method isidentifier():
a =  "30DaysOfPython"
b =  "thirty_days_of_python"
print(a.isidentifier())
print(b.isidentifier())

# The following list contains the names of some of python libraries:
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
pythonLibraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result = '#'.join(pythonLibraries)
print(result)
sentence5 = "I am enjoying this challenge." "I just wonder what is next"
print(sentence5.split('""'))

sentence6 = "Name\t\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsink"
print(sentence6.expandtabs())



