from Animal import Animal


class Cat(Animal):
    def __init__(self, cad_in_picioare, name):
        super().__init__(name)
        self.cad_in_picioare = cad_in_picioare

    @staticmethod
    def speak():
        print('Miau! Miau!')

    def print_name(self):
        print('Cat', self.name)
        super().print_digit()
        print('\n')
