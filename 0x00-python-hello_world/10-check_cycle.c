#include "lists.h"
/**
 * check_cycle - a program function that checks the cycle
 * of linked lists
 * @list: lists the nodes
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *check = list;

	if(!list)
		return (0);

	while (current && check && check->next)
	{
		current = current->next;
                check = check->next->next;
		if (current == check)
			return (1);
		
	}
	return (0);
}
