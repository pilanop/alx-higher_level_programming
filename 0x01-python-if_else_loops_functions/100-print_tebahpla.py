#!/usr/bin/python3
for i in range(122, 64, -1):
    print("{:c}".format(i if i % 2 == 0 else i - 32), end="")
