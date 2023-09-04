#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - sing link list
 * @z: integer
 * @next: points for the next nodes
 *
 * Description: sing linked list for nodes structure
 * Holberton project
 */
typedef struct listint_s
{
	int z;
	struct listint_s *next;
} listint_t;

void free_listint(listint_t *head);
int check_cycle(listint_t *list);
size_t print_listint(const listint_t *h);
listint_t *add_nodeint(listint_t **head, const int n);

#endif

