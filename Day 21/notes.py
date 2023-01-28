class Person:
    def __init__(self, firstName, lastName, age, country, city):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        self.country = country
        self.city = city

    def info(self):
        return f"{self.firstName} {self.lastName} is {self.age} years old. He lives in {self.city}," \
               f" {self.country}"

p = Person('Dennis', 'Njogu', 23, "Kenya", "Nairobi")
print(p.info())