# New Node
class Node:
    def __init__(self, value):
        # Store the value of the node
        self.value = value

        # Pointer to the next node in the linked list (initially None)
        self.next = None


# Linked List
class LinkedList:
    def __init__(self, value):
        # Check if the initial value is None
        if value is None:
            # Initialize an empty linked list with no nodes
            self.head = None
            self.tail = None
            self.length = 0  # Set length to 0 for an empty list
        else:
            # Create a new node with the given value
            new_node = Node(value)

            # Set both head and tail to the new node (only one node in the list)
            self.head = new_node
            self.tail = new_node

            # Initialize the length of the list to 1
            self.length = 1

    def print_linked_list(self):
        """
        This method returns a string representation of the linked list.
        :return: str
        """
        # Initialize an empty string to store the linked list elements
        elements = []

        # Start from the head of the linked list
        current_node = self.head

        # Iterate through the linked list until the current node is None
        while current_node:
            # Append the value of the current node to the elements string
            elements.append(str(current_node.value))

            # Move to the next node in the linked list
            current_node = current_node.next

        # Return the string representation of the linked list
        return elements

    def append_node(self, value):
        """
        This method appends a new node with the given value to the end of the linked list.
        :param value: The value of the new node to be appended
        :return: bool
        """
        # Create a new node with the given value
        new_node = Node(value)

        # Check if the linked list is empty
        if self.head is None:
            # Set both head and tail to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # Update the next pointer of the current tail node
            self.tail.next = new_node

            # Update the tail to the new node
            self.tail = new_node

        # Increment the length of the linked list
        self.length += 1
        return True
