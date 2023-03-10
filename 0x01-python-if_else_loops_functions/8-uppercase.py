#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if int(ord(c)) >= 97 and int(ord(c)) <= 122:
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
