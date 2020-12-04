#
# # from my_package import abc, defg, my_var as mv
# #
# # # from my_package.custom_module import my_function as abc, my_var as mv
# # # from my_package.another_module import my_function as asdgjh
# #
# #
# # if __name__ == '__main__':
# #     print(mv)
# #     abc()
# #     defg()
# #
# #     # def my_function(n):
# #     #     if n < 0:
# #     #         raise ValueError(f'{n} este negativ.')
# #     #
# #     #     print(n)
# #     #
# #     #
# #     # try:
# #     #     my_function(-3)
# #     # except ValueError as e:
# #     #     print(e)
# #
# #     # keyboard_input = input('nr = ')
# #     #
# #     # try:
# #     #     my_number = int(keyboard_input)
# #     #     print(undefined_var)
# #     # except ValueError as e:
# #     #     pass
# #     # except NameError as e:
# #     #     print('caught error', e)
# #     # else:
# #     #     print('else branch')
# #     # finally:
# #     #     print('finally branch')
# #     #     my_number = 0
# #     #
# #     # print(3 + my_number)
# #
# #     # from copy import copy, deepcopy
# #
# #     # def my_function(my_list):
# #     #     # my_copied_list = deepcopy(my_list)
# #     #     # my_list = copy(my_list)
# #     #     # my_list = my_list[:]
# #     #     my_copied_list = my_list.copy()
# #     #     print(id(my_list[2]), id(my_copied_list[2]))
# #     #
# #     #
# #     # main_list = ['abc', 'def', ['aa', 'bbb'], {'a': 1}]
# #     # # print(main_list)
# #     # my_function(main_list)
# #     # # print(main_list)
# #
# #     # [0, 1, 2, 3, 4, 5, ..., n-2, n-1, n]
# #     # def get_sum(n):
# #     #     my_sum = 0
# #     #     my_range = range(n + 1)
# #     #
# #     #     for number in my_range:
# #     #         my_sum += number
# #     #
# #     #     return my_sum
# #     #
# #     #
# #     # print(get_sum(5))
# #     # print(get_sum(7))
# #     # print(get_sum(10))
# #     # print(get_sum(2000))
# #
# #     # [0, 1, 2, 3, 4, 5]
# #     # def get_sum(n):
# #     #     my_sum = 0
# #     #     my_range = range(0, n + 1, 2)
# #     #     print(list(my_range))
# #     #
# #     #     for number in my_range:
# #     #         my_sum += number
# #     #
# #     #     return my_sum
# #
# #     # def get_sum(n):
# #     #     if n == 0:
# #     #         return 0
# #     #
# #     #     return n + get_sum(n-1) if n % 2 == 0 else get_sum(n-1)
# #     #
# #     #
# #     # print(get_sum(5))
# #
# #     # def get_sum(n):
# #     #     if n == 0:
# #     #         return 0
# #     #
# #     #     return n + get_sum(n-1)
# #     #
# #     #
# #     # print(get_sum(5))
# #
# #     # if 3 < 5:
# #     #     my_var = 'abc'
# #     # else:
# #     #     my_var = 'def'
# #     # my_var = 'abc' if 3 > 5 else 'def'
# #     #
# #     # print(my_var)
# #
# #     # def get_sum_of_numbers(*args):
# #     #     my_sum = 0
# #     #
# #     #     for number in args:
# #     #         my_sum += number
# #     #
# #     #     return my_sum
# #     #
# #     #
# #     # my_sum = get_sum_of_numbers()
# #     #
# #     # print('my_sum =', my_sum)
# #
# #     # my_list = [5, 7, 8, 1, 7]
# #     #
# #     # index = 0
# #     # while index < len(my_list):
# #     #     print(f'Elementul {my_list[index]} se afla pe pozitia {index}')
# #     #     index += 1
# #     #
# #     # for index, element in enumerate(my_list):
# #     #     print(f'Elementul {element} se afla pe pozitia {index}')
# #     #
# #     # print('the end')
#
#
# # return 15, 6, 9
# # def rec_sum(n):
# #     if n == 0:
# #         return 0, 0, 0
# #
# #     total_sum, even_sum, odd_sum = rec_sum(n - 1)
# #     total_sum += n
# #
# #     if n % 2 == 0:
# #         even_sum += n
# #     else:
# #         odd_sum += n
# #
# #     return total_sum, even_sum, odd_sum
# #
# #
# # total_sum, even_sum, odd_sum = rec_sum(5)
# # # total_sum, even_sum, odd_sum = rec_sum(5)  # total_sum, even_sum, odd_sum = 15, 6, 9
# # print(total_sum, even_sum, odd_sum)  # 15, 6, 9
#
# # def my_sum(a, b):
# #     return a + b
# # my_sum = lambda a, b: a + b
# # def sort_by_key(x):
# #     return x['rank']
#
#
# # players = [{
# #     'first_name': 'A1',
# #     'last_name': 'B1',
# #     'rank': 3,
# # }, {
# #     'first_name': 'A2',
# #     'last_name': 'B2',
# #     'rank': 1
# # }, {
# #     'first_name': 'A3',
# #     'last_name': 'B3',
# #     'rank': 2
# # }, {
# #     'first_name': 'A4',
# #     'last_name': 'B4',
# #     'rank': 4
# # }, {
# #     'first_name': 'A5',
# #     'last_name': 'B5',
# #     'rank': 5
# # }]
# #
# # sorted_players = sorted(players, key=lambda x: x['rank'])
# # # print('sorted_players', sorted_players)
# #
# #
# # def map_list(player):
# #     rank = player['rank']
# #
# #     if rank <= 3:
# #         player['is_top_3'] = True
# #     else:
# #         player['is_top_3'] = False
# #
# #     return player
# #
# #
# # players_with_top_3 = map(map_list, sorted_players)
# # print('players_with_top_3', list(players_with_top_3))
# #
# #
# # top_3_players = filter(lambda player: player['rank'] <= 3, sorted_players)
# # print('type(top_3_players)', type(top_3_players))
# # print('list(top_3_players)', list(top_3_players))
#
# list_1 = [1, 2, 3, 4, 5]
# list_2 = list(map(lambda x: x ** 2, list_1))  # [1, 4, 9, 16, 25]
# # [(1, 1), (2, 4), ....]
# list_3 = [0, 0]
#
# my_zip = zip(list_1, list_3, list_2)  # *args
# print('my_zip', my_zip, type(my_zip))
# print('list(my_zip)', list(my_zip))
#
# users = ['a', 'b', 'c']
# cars = ['c1', 'c2', 'c3']
# for user, car in zip(users, cars):
#     print(f'userul {user} cumpara masina {car}')
#
# dict_keys = ['key_1', 'key_2', 'key_3', 'key_3']
# dict_values = ['val_1', 'val_2', 'val_3', 'val_4']
# my_dict = dict(zip(dict_keys, dict_values))
# print('type(my_dict)', type(my_dict), my_dict)
#
# x = {
#     'key_1': 'val_1',
#     'key_2': 'val_2',
#     'key_3': 'val_3',
#     'key_3': 'val_4',
# }
#
# print(x)
#
# # my_dict = {}
# # for key_index, dict_key in enumerate(dict_keys):
# #     if key_index < len(dict_values):
# #         my_dict[dict_key] = dict_values[key_index]
# #
# # print('my_dict', my_dict)


keys = ['a', 'b', 'c', 'd', 'e']
list_1 = [1, 2, 3, 4, 5]  # [2, 4]

list_2 = [element ** 2 if element % 2 == 0 else -element for element in list_1 if element < 3]
print(type(list_2), list_2)

my_dict = {
    my_key: my_element
    for my_key, my_element in zip(keys, list_1) if my_element % 2 == 0
}

print('my_dict', type(my_dict), my_dict)
