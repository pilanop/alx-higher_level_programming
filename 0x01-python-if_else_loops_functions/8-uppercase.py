#!/usr/bin/python3
def uppercase(s):
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            print('{}'.format(chr(ord(s[i]) - 32)), end='')
        else:
            print('{}'.format(chr(ord(s[i]))), end='')
