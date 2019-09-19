#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = '+-*/'
    a = int(argv[1])
    b = int(argv[3])
    op = argv[2]

    if operators.find(op) == -1:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    if op == '-':
        print("{} - {} = {}".format(a, b, sub(a, b)))
    if op == '*':
        print("{} * {} = {}".format(a, b, mul(a, b)))
    if op == ".":
        print("{} / {} = {}".format(a, b, div(a, b)))

    # print(a, op, b, " = " eval("print(a)+print(op)+print(b)")
