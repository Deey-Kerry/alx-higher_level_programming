#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    output = 0
    previous_value = 0

    for char in roman_string[::-1]:
        value = roman_values.get(char, 0)

        if value >= previous_value:
            output += value
        else:
            output -= value

        previous_value = value

    return output
