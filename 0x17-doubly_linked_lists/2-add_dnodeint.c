#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * add_dnodeint - add nodes to top of list
 * @head: the list
 * @n: new node value
 *
 * Return: pointer to new list
 */

dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	/* size_t i; */
	dlistint_t *new;
	dlistint_t **h1 = head;

	/* head = &hello; */
	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
	{
		dprintf(2, "Error: Can't malloc\n");
		return (0);
	}
	new->n = n;
	/* *h1->prev = new; */
	new->next = *h1;
	new->prev = NULL;
	*h1 = new;

	return (*h1);
}
