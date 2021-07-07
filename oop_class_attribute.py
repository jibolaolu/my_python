class Dog():
    species = 'mammal'
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

    def bark(self):
        print('Woof Woof my name is {}'.format(self.name))


my_dog = Dog(breed = 'French-Mastiff', name = 'Sparrow', age= 23)
my_dog.bark()

brd = my_dog.breed
print(brd)


class Place():
    country = 'United Kingdom'
    def __init__(self, county, road):
        self.county = county
        self.road = road

    def where_from(self):
        print('I live on {} road within the {} borough in {}'.format(self.road, self.county, self.country))

pl = Place(county='Kent',road = 'Canterbury')
cntry = pl.country
print(cntry)
p = pl.road
print(p)
pl.where_from()

