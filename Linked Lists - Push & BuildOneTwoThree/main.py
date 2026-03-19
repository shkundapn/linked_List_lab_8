from preloaded import Node

def push(head, data):
    """
    Creates a new node with the given data and pushes it onto the front
    of the linked list.

    Args:
        head: The current head node of the linked list.
        data: The value to be stored in the newly created node.

    Returns:
        Node: The newly created head node, pointing to the previous head.
    """
    curr = Node(data)
    curr.next = head
    return curr

def build_one_two_three():
    """
    Constructs a linked list sequentially containing the values 1, 2, and 3.

    Returns:
        Node: The head node (value 1) of the constructed linked list
              (1 -> 2 -> 3 -> None).
    """
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
