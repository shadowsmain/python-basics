import sys

my_var = [12, '15', 95.32, 55, True]  # var -> reference
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = 12
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = 12.5
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))

my_var = '12.5'
print(my_var, type(my_var), id(my_var), sys.getsizeof(my_var))