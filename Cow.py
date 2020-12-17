from Animal import Animal, MyClass


class Cow(Animal, MyClass):
    @staticmethod
    def speak():
        print('Muu! Muu!')

    def print_name(self):
        print('Cow', self.name)
        super().print_digit()
        print('\n')
