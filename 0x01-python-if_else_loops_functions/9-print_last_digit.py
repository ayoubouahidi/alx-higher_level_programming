#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    a = number % 10
    if number == 1:
        number *= -1
    print("{:d}".format(a), end="")
    return a
