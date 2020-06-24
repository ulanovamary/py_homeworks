def my_func(arg_1, arg_2, arg_3):
    my_list = [arg_1, arg_2, arg_3]
    max_arg_1 = max(my_list)
    my_list.remove(max_arg_1)
    max_arg_2 = max(my_list)
    result = max_arg_1 + max_arg_2
    return result

a = 0
b = 1
c = 2

print(my_func(a, b, c))
