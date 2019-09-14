#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 *  get_dnodeint_at_index - return node # index
 * @head: double point. ???
 * @index: node value to return
 *
 * Return: pointer to new list
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	/* listint_t *new; */
	dlistint_t *current;
	unsigned int len = 0;

	if (head) /* Then find the last node */
	{
		current = head;
		while (current)
		{
			if (index == len)
				return (current);
			len++;
			current = current->next;
		}
	}

	return (NULL);
}
