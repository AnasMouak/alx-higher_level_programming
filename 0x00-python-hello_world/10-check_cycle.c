#include "lists.h"

/**
 * check_cycle - Check if a singly linked list has a cycle.
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 otherwise.
 */

int check_cycle(listint_t *list)
{
	listint_t *s, *f;

	if (list == 0)
	{
		return (0);
	}
	s = list;
	f = list->next;

	while (f != 0 && f->next != 0)
	{
		if (s == f)
		{
			return (1);
		}
		s = s->next;
		f = f->next->next;
	}
	return (0);
}
