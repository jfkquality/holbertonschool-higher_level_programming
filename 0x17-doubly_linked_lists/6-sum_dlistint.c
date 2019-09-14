#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>
#include "lists.h"

/**
 *  sum_dlistint - sum a list's values
 * @head: double point.
 *
 * Return: pointer to new list
 */
int sum_dlistint(dlistint_t *head)
{
	/* listint_t *new; */
	dlistint_t *current;
	int sum = 0;


	if (head) /* Then find the last node */
	{
		current = head;
		while (current)
		{
			sum += current->n;
			current = current->next;
		}
	}
	else
		return (0);

	return (sum);
}
