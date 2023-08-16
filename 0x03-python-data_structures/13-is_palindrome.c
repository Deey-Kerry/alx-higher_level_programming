#include "lists.h"
#include <stdlib.h>
#include <stdio.h>
/**
 * reverse_listint - A program function that reverses a singly linked
 * list
 * @head: A pointer
 * Return: reversed singly linked list
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *node = *head, *next, *prev = NULL;

	while (node)
	{
		next = node->next;
		node->next = prev;
		prev = node;
		node = next;
	}
	*head = prev;
	return (*head);
}
/**
 * is_palindrome - A program function that checks if a singly
 * linked list is a palindrome
 * @head: A pointer
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	size_t size = 0, a;
	listint_t *temp, *prev, *current;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	temp = *head;
	while (temp)
	{
		size++;
		temp = temp->next;
	}
	temp = *head;
	a = 0;
	while (a < (size/2) - 1)
	{
		a++;
		temp = temp->next;
	}
	if ((size % 2) == 0 && temp->n != temp->next->n)
		return (0);
	temp = temp->next->next;
	prev = reverse_listint(&temp);
	current = prev;

	temp = *head;
	while (prev)
	{
		if (temp->n != prev->n)
			return (0);
		temp = temp->next;
		prev = prev->next;
	}
	reverse_listint(&current);
	return (1);
}
