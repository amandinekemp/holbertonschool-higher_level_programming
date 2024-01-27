#!/usr/bin/python3

def uppercase(str):
    for char in str:
        ascii_value = ord(char) - 32 if 97 <= ord(char) <= 122 else ord(char)
        print("{:c}".format(ascii_value), end="")
    print()
    