#include "lists.h"

/**
* insert_node - Inserts the number into a sort singly-link list.
* @head: Pointer the head of linked list.
* @number: The number to inserts.
*
* Return: If function fail - NULL.
* Otherwise - Pointer to the new node.
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *node = *head, *new;

new = malloc(sizeof(listint_t));
if (new == NULL)
return (NULL);
new->n = number;

if (node == NULL || node->n >= number)
{
new->next = node;
*head = new;
return (new);
}

while (node && node->next && node->next->n < number)
node = node->next;

new->next = node->next;
node->next = new;

return (new);
}

