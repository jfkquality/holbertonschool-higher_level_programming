#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
	{
		printf("Error\n");
		return (NULL);
	}
	new->n = number;
	new->next = NULL;
	if (current == NULL)
	{
		*head = new;
		return (new);
	}
	if ((*head)->n > number)
	{
		new->next = *head;
		*head = new;
		return (new);
	}
	while (current)
	{
		if (current->next != NULL)
		{
			if (current->next->n > number) /*insert new b4 next*/
			{
				new->next = current->next;
				current->next = new;
				return (new);
			}
		}
		else
		{
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
