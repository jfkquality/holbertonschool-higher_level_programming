#!/usr/bin/python3

# If the reverse of a number is less than the number, it's a dup; don't print it.
# Reverse a number buy mod 10 times 10 plus quotient of divide by 10

for i in range(0, 89):
    # print("{:02d} {:02d}".format(i, ((i % 10 * 10) + (i // 10))))
    if i < (i % 10 * 10) + (i // 10) and i != (i % 10 * 10) + (i // 10):
        print("{:02d}".format(i), end=', ')
for i in range(80, 99):
    if i < (i % 10 * 10) + (i // 10) and i != (i % 10 * 10) + (i // 10):
        print("{:02d}".format(i))

