#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_list_integer(my_list)
    print('\n')
    my_list.append(5)
    print_list_integer(my_list)
    print('\n')
    my_list += [6, 5, 4, 3, 2, 1]
    print_list_integer(my_list)
    print('\n')
