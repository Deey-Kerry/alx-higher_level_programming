#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """a function that divides element by element 2 lists"""
    new_list = []
    for i in range(0, list_length):
        try:
            tmp_result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("Wrong type")
            tmp_result = 0
        except ZeroDivisionError:
            print("division by 0")
            tmp_result = 0
        except IndexError:
            print("out of range")
            tmp_result = 0
        finally:
            new_list.append(tmp_result)
        return (new_list)
