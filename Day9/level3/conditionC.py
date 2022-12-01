person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

middle = float(len(person)-1)/2
frontEnd = ['Javascript']

if len(person['skills']) != 0:
    print(person['skills'][int(middle)])
    if person['skills'].__contains__('Python'):
        print("You have Python in the list")

if 'Javascript' in person['skills'] or 'React' in person['skills']:
    print("FrontEnd Developer")
elif 'Python' in person['skills'] or 'Node' in person['skills'] or 'MongoDb' in person['skills']:
    print("BackEnd Developer")
else:
    print("FullStack Developer")

if person['is_marred'] == True and person['country'] == 'Finland':
    print("Dennis lived in Finland. He is married")