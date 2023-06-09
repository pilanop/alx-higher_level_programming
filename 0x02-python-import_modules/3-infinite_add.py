#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    args = sys.argv[1:]
    num_args = len(args)
    sum = 0
    for i in range(num_args):
        sum += int(args[i])
print(sum)
