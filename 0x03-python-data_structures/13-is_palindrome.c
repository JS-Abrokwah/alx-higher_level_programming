#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - checks if a list is a palindrome
 * @head: the list input
 * Return: 0 if not palindrome, else 1
 *
 */
int is_palindrome(listint_t **head)
{
	listint_t *left, *right, *current, *prev, *temp;

	left = *head;
	right = *head;
	/*
	 * find the middle of palindrome
	 */
	while (right != NULL && right->next != NULL)
	{
		left = left->next;
		right = right->next->next;
	}

	/*
	 * reverse the right side of the list
	 */
	prev = NULL;
	current = left;
	while (current != NULL)
	{
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}
	/*
	 * compare the two sides
	 */
	left = *head;
	right = prev;
	while (right != NULL)
	{
		if (left->n != right->n)
			return (0);
		left = left->next;
		right = right->next;
	}
	return (1);
}
