#!/usr/bin/python3
def best_score(a_dictionary):
    my_list = []
    if a_dictionary is None:
        return None

    for i in a_dictionary.items():
        pair = list(i)
        my_list.append(tuple(pair))

    people = my_list

    highest = max(people, key=lambda x: x[1])
    return highest[0]
