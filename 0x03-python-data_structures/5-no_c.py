#!/usr/bin/python3
def no_c(my_string):
    no_C = ""
    for a in range(len(my_string)):
        if (my_string[a] != 'c' and my_string[a] != 'C'):
            no_C
    return (no_C)
