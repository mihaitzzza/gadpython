class MyIterator:
    def __init__(self, n, name):
        self.n = n
        self.name = name

    def __iter__(self):
        self.value = 0
        print(self.name)
        return self

    def __next__(self):
        if self.value < self.n:
            value = self.value
            self.value += 1
            return value
        else:
            raise StopIteration


iterator_instance = MyIterator(5, 'abc')
# my_iterable = iter(iterator_instance)
# for i in my_iterable:
#     print(i)

print('\n')
print(iterator_instance.name)
print('\n')

my_list = set(iter(iterator_instance))
print(type(my_list))
for a in my_list:
    print(a)

