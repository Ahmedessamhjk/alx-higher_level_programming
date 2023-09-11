#!/usr/bin/python3
def no_c(my_string):
    no_c = ""
    for a in range(len(my_string)):
        if (my_string[a] != 'c' and my_string != 'C'):
            no_c += my_string[a]
    return (no_c)
