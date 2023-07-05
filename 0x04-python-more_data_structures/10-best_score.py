#!/usr/bin/python3
def best_score(a_dictionary):
    highest = 0
    highest_name = ''

    if a_dictionary is None:
        return None

    for i in a_dictionary.items():
        pair = list(i)
        if pair[1] > highest:
            highest = pair[1]
            highest_name = pair[0]

    return highest_name
