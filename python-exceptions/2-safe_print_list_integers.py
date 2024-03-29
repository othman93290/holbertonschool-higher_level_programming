#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for value in my_list[:x]:
            if type(value) == int:
                print("{:d}".format(value), end=" ")
                count += 1
    except ValueError and TypeError:
        return
    else:
        print()
        return count
