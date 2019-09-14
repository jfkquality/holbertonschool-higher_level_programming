#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 * insert_dnodeint_at_index - insert node at index
 * @h: double point.
 * @idx: node value to return
 * @n: index
 *
 * Return: pointer to new list
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	unsigned int node = 0;
	dlistint_t *current;
	dlistint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		printf("Error\n");
		return (NULL);
	}

	new->n = n;

	if (*h)
	{
		if (idx == 0)
		{
			new->next = *h;
			*h = new;
			return (*h);
		}

		current = *h;
		/* node = 1; */
		while (current)
		{
			if (node == idx - 1)
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
			node++;
			current = current->next;
		}
	}

	return (NULL);
}
