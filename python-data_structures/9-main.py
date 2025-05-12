#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 9, 2, 13, 34, 90, -13, 91]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))