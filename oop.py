from Cat import Cat
from Dog import Dog
from Cow import Cow


my_cat = Cat(True, name='Julia')
# my_cat.speak()

my_dog = Dog(name='Juliu')
# my_dog.speak()

my_cow = Cow(name='Milka')
# my_cow.speak()
print(my_cow.get_name())

animals = [my_cat, my_dog, my_cow]
for animal in animals:
    animal.print_name()
