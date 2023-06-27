#!/usr/bin/python3
class Node:
    """
    This class represents a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a node with a given data value and next node.

        Args:
            data (int): The data value of the node.
            next_node (Node): The next node in the linked list

        Raises:
            TypeError: If data is not an integer.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Getter method to retrieve the data value of the node.

        Returns:
            int: The data value of the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method to set the data value of the node.

        Args:
            value (int): The data value to set.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

        self.__data = value

    @property
    def next_node(self):
        """
        Getter method to retrieve the next node in the linked list.

        Returns:
            Node: The next node in the linked list.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method to set the next node in the linked list.

        Args:
            value (Node): The next node to set.

        Raises:
            TypeError: If value is not None or a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")

        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.
    """

    def __init__(self):
        """
        Initializes an empty singly linked list.
        """
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the list.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)

        if self.head is None:
            # Case: The list is empty, make the new node the head
            self.head = new_node
        elif value < self.head.data:
            # Case: The new node should be the new head
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head

            while current.next_node is not None and value >= current.next_node.data:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        nodes = []
        current = self.head

        while current is not None:
            nodes.append(str(current.data))
            current = current.next_node

        return "\n".join(nodes)
