#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) != str:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}

    values = [roman_values[x] for x in roman_string] + [0]
    output = 0

    for i in range(len(values) - 1):
        if values[i] >= values[i+1]:
            output += values[i]
        else:
            output -= values[i]

    return output
