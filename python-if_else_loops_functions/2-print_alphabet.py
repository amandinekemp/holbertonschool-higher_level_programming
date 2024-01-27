#!/usr/bin/python3

for ascii_value in range(97, 123):
    #"{:c}".format(ascii_value) est utilisée pour formater le nombre comme un caractère (lettre).
    print("{:c}".format(ascii_value), end="")
