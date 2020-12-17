from abc import abstractmethod


class MyClass():
    @staticmethod
    def get_name():
        return 4


class Animal:
    legs = 4

    def __init__(self, name, color=None, breed=None):
        self.__name = name
        self.color = color
        self.breed = breed

    def __str__(self):
        return f'{type(self)}: {self.__name}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @staticmethod
    @abstractmethod
    def speak():
        pass

    def print_digit(self):
        print('Animal', 4)
