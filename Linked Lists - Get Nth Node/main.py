from preloaded import Node

def get_nth(node, index):
    """
    Retrieves the node at the specified index in a linked list.

    Args:
        node: The starting head node of the linked list.
        index: The zero-based integer index of the node to retrieve.

    Returns:
        Node: The node located at the given index.

    Raises:
        IndexError: If the index is negative, or if the index is out of bounds
                    (greater than or equal to the length of the list).
    """
    if index < 0 or node is None:
        raise IndexError

    while index > 0:
        node = node.next
        index -= 1

    if node is None:
        raise IndexError

    return node
