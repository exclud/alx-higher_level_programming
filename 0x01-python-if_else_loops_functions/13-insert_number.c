#include <stdlib.h>
#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: the number to insert
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node;
    listint_t *current;

    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    new_node->n = number;
    new_node->next = NULL;

    if (*head == NULL || (*head)->n >= new_node->n)
    {
        new_node->next = *head;
        *head = new_node;
    }
    else
    {
        current = *head;
        while (current->next != NULL && current->next->n < new_node->n)
        {
            current = current->next;
        }
        new_node->next = current->next;
        current->next = new_node;
    }
    return (new_node);
}
