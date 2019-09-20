#!/usr/bin/python3
import ast
from sys import argv
# from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    argc = len(argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = "+-x/"
    a = (argv[1])
    b = (argv[3])
    op = argv[2]

    if operators.find(op) == -1:
        print("Unknown operator. Available operators: +, -, x and /")
        exit(1)

    if op == "x":
        op = "*"

    print("{} {} {} = {}".format(a, op, b, ast.literal_eval(a + op + b)))

    # if op == "+":
        # print("{} {} {} = {}".format(a, op, b, add(a, b)))
    # if op == '-':
    #     print("{} {} {} = {}".format(a, op, b, sub(a, b)))
    # if op == '*':
    #     print("{} {} {} = {}".format(a, op, b, mul(a, b)))
    # if op == "/":
    #     print("{} {} {} = {}".format(a, op, b, div(a, b)))

    # print(a, op, b, " = " eval("print(a)+print(op)+print(b)")
