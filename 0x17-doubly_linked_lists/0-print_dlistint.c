#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * print_dlistint - print linked list
 * @h: the linked list
 *
 * Return: counter
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t i;
	dlistint_t h1 = *h;

	while (h1.next)
	{
		printf("%d\n", h1.n);
		h1 = *h1.next;
		i++;
	}
	i++;
	printf("%d\n", h1.n);
	return (i);
}
