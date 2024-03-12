#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        x = ord(str[i])
        if x not in [65, 90]:
            x = x - 32
        print("{}".format(chr(x)), end="")
            
