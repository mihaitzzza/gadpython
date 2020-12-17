from Animal import Animal


class Dog(Animal):
    @staticmethod
    def speak():
        print('Ham! Ham!')

    def print_name(self):
        print('Dog', self.name)
        super().print_digit()
        print('\n')

