#include "lists.h"

int is_palindrome(listint_t **head)
{
	listint_t *start, *end;

	if (*head == 0 || (*head)->next == 0)
	{
		return (1);
	}
	start = *head;
	end = NULL;

	while (start != 0 && end != 0)
	{
		if (start != end)
		{
			return (0);
		}
		start = start->next;
		end = end->next;
	}
	return (1);


}
