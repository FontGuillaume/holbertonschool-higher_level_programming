#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for i in a_dictionary:
        valeur = a_dictionary[i]
        new_dictionary[i] = valeur * 2
    return new_dictionary
