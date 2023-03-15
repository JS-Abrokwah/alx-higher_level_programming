#!/usr/bin/python3
def uniq_add(my_list=[]):
    new = [my_list[:1]]
    for i in my_list:
        if i is not in new:
            new.append(i)
    add = 0
    for i in new:
        add += i
    return add
