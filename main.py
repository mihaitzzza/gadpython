from my_package import abc, defg, my_var as mv

# from my_package.custom_module import my_function as abc, my_var as mv
# from my_package.another_module import my_function as asdgjh


if __name__ == '__main__':
    print(mv)
    abc()
    defg()

    # def my_function(n):
    #     if n < 0:
    #         raise ValueError(f'{n} este negativ.')
    #
    #     print(n)
    #
    #
    # try:
    #     my_function(-3)
    # except ValueError as e:
    #     print(e)

    # keyboard_input = input('nr = ')
    #
    # try:
    #     my_number = int(keyboard_input)
    #     print(undefined_var)
    # except ValueError as e:
    #     pass
    # except NameError as e:
    #     print('caught error', e)
    # else:
    #     print('else branch')
    # finally:
    #     print('finally branch')
    #     my_number = 0
    #
    # print(3 + my_number)

    # from copy import copy, deepcopy

    # def my_function(my_list):
    #     # my_copied_list = deepcopy(my_list)
    #     # my_list = copy(my_list)
    #     # my_list = my_list[:]
    #     my_copied_list = my_list.copy()
    #     print(id(my_list[2]), id(my_copied_list[2]))
    #
    #
    # main_list = ['abc', 'def', ['aa', 'bbb'], {'a': 1}]
    # # print(main_list)
    # my_function(main_list)
    # # print(main_list)

    # [0, 1, 2, 3, 4, 5, ..., n-2, n-1, n]
    # def get_sum(n):
    #     my_sum = 0
    #     my_range = range(n + 1)
    #
    #     for number in my_range:
    #         my_sum += number
    #
    #     return my_sum
    #
    #
    # print(get_sum(5))
    # print(get_sum(7))
    # print(get_sum(10))
    # print(get_sum(2000))

    # [0, 1, 2, 3, 4, 5]
    # def get_sum(n):
    #     my_sum = 0
    #     my_range = range(0, n + 1, 2)
    #     print(list(my_range))
    #
    #     for number in my_range:
    #         my_sum += number
    #
    #     return my_sum

    # def get_sum(n):
    #     if n == 0:
    #         return 0
    #
    #     return n + get_sum(n-1) if n % 2 == 0 else get_sum(n-1)
    #
    #
    # print(get_sum(5))

    # def get_sum(n):
    #     if n == 0:
    #         return 0
    #
    #     return n + get_sum(n-1)
    #
    #
    # print(get_sum(5))

    # if 3 < 5:
    #     my_var = 'abc'
    # else:
    #     my_var = 'def'
    # my_var = 'abc' if 3 > 5 else 'def'
    #
    # print(my_var)

    # def get_sum_of_numbers(*args):
    #     my_sum = 0
    #
    #     for number in args:
    #         my_sum += number
    #
    #     return my_sum
    #
    #
    # my_sum = get_sum_of_numbers()
    #
    # print('my_sum =', my_sum)

    # my_list = [5, 7, 8, 1, 7]
    #
    # index = 0
    # while index < len(my_list):
    #     print(f'Elementul {my_list[index]} se afla pe pozitia {index}')
    #     index += 1
    #
    # for index, element in enumerate(my_list):
    #     print(f'Elementul {element} se afla pe pozitia {index}')
    #
    # print('the end')
