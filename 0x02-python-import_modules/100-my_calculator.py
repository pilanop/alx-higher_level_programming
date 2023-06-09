#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

args = sys.argv[1:]
num_args = len(args)
if num_args != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)
a = int(args[0])
b = args[1]
c = int(args[2])
if num_args == 3 and b == "+":
    print("{} + {} = {}".format(a, c, add(a, c)))
elif num_args == 3 and b == "-":
    print("{} - {} = {}".format(a, c, sub(a, c)))
elif num_args == 3 and b == "*":
    print("{} * {} = {}".format(a, c, mul(a, c)))
elif num_args == 3 and b == "/":
    print("{} / {} = {}".format(a, c, div(a, c)))
elif num_args == 3 and b not in ["+", "-", "*", "/"]:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)
