def sum_decorator_with_value(value):
    def sum_decorator(my_function):
        def wrapper(x, y):
            result = my_function(x, y)
            return result ** value

        return wrapper

    return sum_decorator


@sum_decorator_with_value(2)
def my_sum(a, b):
    return a + b


@sum_decorator_with_value(3)
def my_function(a, b):
    return a - b


print(my_sum(2, 3))
