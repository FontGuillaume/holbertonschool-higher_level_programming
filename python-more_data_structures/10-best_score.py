#!/usr/bin/python3
def best_score(a_dictionary):
    best_key = None
    high_score = -1
    if a_dictionary is None:
        return None
    for i in a_dictionary.keys():
        if a_dictionary[i] > high_score:
            high_score = a_dictionary[i]
            best_key = i
    return best_key
