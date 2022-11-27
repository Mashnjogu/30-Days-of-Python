fruites = ('Banana', 'Orange', 'Strawberry')
vegetables = ('Cabbage', 'Carrots', 'Kales')
animal_products = ('Dairy Meal', 'Proteins', 'Salt')
food_stuffs_tp = fruites + vegetables + animal_products
print(food_stuffs_tp)
food_stuffs_lt = list(food_stuffs_tp)
print(food_stuffs_lt)
middleItem = int(len(food_stuffs_lt)//2)
food_stuffs_lt.remove(food_stuffs_lt[middleItem])
print(food_stuffs_lt)
del food_stuffs_lt[0:3]
print(food_stuffs_lt)
del food_stuffs_lt[-4:-1]
print(food_stuffs_lt)
del food_stuffs_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)
