#!/usr/bin/python3
def roman_to_int(roman_string):
    """a function that converts a Roman numeral to an integer"""
    if roman_string is None or type(roman_string)!= str:
        return 0
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100,
            'D': 500, 'M': 1000}
    value = [roman_values[x] for x in roman_string] + [0]
    output = 0

    for char in range(len(value)- 1):
        if value[char] >= value[char + 1]:
            output += value[char]
        else:
            output -= value[char]
    
    return (output)
