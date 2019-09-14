#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include "lists.h"

/**
 * free_dlistint - free a list
 * @head: the list
 *
 * Return: pointer to new list
 */
void free_dlistint(dlistint_t *head)
{
        dlistint_t *next;
        dlistint_t *current;

        current = head;
        while (current)
        {
                next = current->next;
                /* free(current.n); */
                free(current);
                current = next;
        }
}
