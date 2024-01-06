#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *p, *t, *prev;

	t = malloc(sizeof(listint_t));
	if (t == 0)
	{
		return (0);
	}
	
	t->n = number;
	t->next = NULL;
	
	p = *head;
	prev = NULL;

	while (*head != 0 && p->n < number)
	{
		prev = p;
		p = p->next;
	}
	if (prev == 0)
	{
		t->next = *head;
		*head = t;
	}
	else
	{
		t->next = prev->next;
		prev->next = t;
	}

	return (t);
}
