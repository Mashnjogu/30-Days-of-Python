players = []
countries = ['Algeria', 'Belgium', 'Kenya', 'Canada', 'Uganda']
print(len(countries))
print('The first item is', countries[0],'The middle item is', countries[len(countries)//2],
      'The last item is', countries[len(countries) - 1])

mixed_data_types = ["Dennis", 23, 169, "Single", "1467 - Nyahururu"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle","Amazon"]
print(it_companies)
print(len(it_companies))
print('The first item is', it_companies[0],'The middle item is', it_companies[len(it_companies)//2],
      'The last item is', it_companies[len(it_companies) - 1])
it_companies[2] = "IBM"
print(it_companies)
it_companies_withHash = '#'.join(it_companies)
print(it_companies_withHash)
does_exits = 'Google' in it_companies
print("Does the company exist?: ", does_exits)
sorted_companies = it_companies.sort(reverse= True)
print("In sorted order",sorted_companies)

#slicing out
first_three = it_companies[0:3]
last_three = it_companies[-3: ]
# middle = it_companies[len(it_companies)//2:len(it_companies)//2]
print(it_companies)
print(first_three)
print(it_companies)
print(last_three)
# print(middle)
del it_companies[0]
print(it_companies)
del  it_companies[len(it_companies)//2]
print(it_companies)
it_companies.pop()
print(it_companies)
it_companies.clear()
print(it_companies)
del it_companies
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
fullstack = front_end + back_end
print(fullstack)
fullstack.insert(5, "Python")
fullstack.insert(6, "SQL")
print(fullstack)

