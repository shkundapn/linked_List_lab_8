def stringify(node):
    """
    Converts a linked list into a formatted string representation.

    Args:
        node: The starting head node of the linked list.

    Returns:
        str: A string showing the connected nodes separated by arrows,
             ending with "None" (e.g., "1 -> 2 -> 3 -> None").
    """
    res = ''
    while node:
        res += str(node.data) + " -> "
        node = node.next
    res += "None"
    return res
