#include <stdlib.h>
#include "lists.h"

/**
 * reverse_list - function that reverses a singly linked list
 * @head: double pointer to the head of the singly linked list
 *
 * Return: a pointer to the first node of the reversed list
 */
listint_t *reverse_list(listint_t **head)
{
    listint_t *prev = NULL;
    listint_t *current = *head;
    listint_t *next;
    while (current != NULL) {
        next  = current->next;  
        current->next = prev;   
        prev = current;
        current = next;
    }
    *head = prev;
    return (*head);
}

/**
 * is_palindrome - function that checks if a singly linked list is a palindrome
 * @head: double pointer to the head of the singly linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *tmp, *rev, *mid;
    int len = 0, i = 0;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    tmp = *head;
    while (tmp != NULL)
        tmp = tmp->next, len++;
    mid = *head;
    for (i = 0; i < len / 2; i++)
        mid = mid->next;
    if (len % 2 != 0 && mid != NULL)
        mid = mid->next;
    rev = reverse_list(&mid);
    tmp = *head;
    while (rev != NULL)
    {
        if (tmp->n != rev->n)
            return (0);
        tmp = tmp->next;
        rev = rev->next;
    }
    return (1);
}
