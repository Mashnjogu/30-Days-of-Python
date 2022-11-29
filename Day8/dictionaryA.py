#A dictionary is a collection of unordered, mutable, key-pair values
dog = {}
dog["name"] = "Wito"
dog["color"] = "Black"
dog["breed"] = "Half Mutina- Half German Shephard"
dog["legs"] = 4
dog["age"] = 2

student_dictionary = {
    'first_name': '',
    'last_name': '',
    'gender': '',
    'age':0,
    'maritial_status': '',
    'skills': [],
    'country': '',
    'city': '',
    'address': ''
}
print("Length of student_dictionary is: ", len(student_dictionary))
student_dictionary['skills'].append('Android')
student_dictionary['skills'].append('Python')
print(student_dictionary['skills'])
student_dictionary_keys = student_dictionary.keys()
student_dictionary_keys_list = list(student_dictionary_keys)
print(student_dictionary_keys_list)

student_dictionary_values = student_dictionary.values()
student_dictionary_values_list = list(student_dictionary_values)
print(student_dictionary_values_list)
#Change the dictionary to a list of tuples using items() method
print(student_dictionary.items())
# Delete one of the items in the dictionary
student_dictionary.pop('maritial_status')
print(student_dictionary)
del dog