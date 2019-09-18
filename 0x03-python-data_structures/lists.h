#ifndef _LISTS_H
#define _LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for Holberton project
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);
void free_listint(listint_t *head);
int check_cycle(listint_t *list);

def islower(c)
def uppercase(str)
def print_last_digit(number)
def add(a, b)
def pow(a, b)
def fizzbuzz()
def remove_char_at(str, n)
def sub(a, b)
def mul(a, b)
def div(a, b)

def print_list_integer(my_list=[])
def element_at(my_list, idx)
def replace_in_list(my_list, idx, element)
def print_reversed_list_integer(my_list=[])
def new_in_list(my_list, idx, element)
def no_c(my_string)
def print_matrix_integer(matrix=[[]])
def add_tuple(tuple_a=(), tuple_b=())
def max_integer(my_list=[])
def divisible_by_2(my_list=[])
def delete_at(my_list=[], idx=0)

#endif
