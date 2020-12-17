from Animal import Animal


class Snake(Animal):
    @staticmethod
    def speak():
        print('Sssss!')

    def print_name(self):
        print('Snake', self.name)
        super().print_digit()
        print('\n')

