#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            print(my_list=[], end=' ')
            count += 1
    except indexError:
        pass
    print()
    return count

