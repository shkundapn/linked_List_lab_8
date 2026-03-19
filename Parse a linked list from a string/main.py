from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    """
    Converts a string representation of a linked list into actual Node objects.

    Args:
        list_repr (str): A string representing the linked list, formatted
                         with values separated by " -> " and ending with "None".
                         Example: "1 -> 2 -> 3 -> None"

    Returns:
        Node | None: The head node of the newly created linked list, or None
                     if the input string represents an empty list ("None").
    """
    lst = list_repr.split(" -> ")
    head = prev = Node(0)

    for i, item in enumerate(lst):
        if item == "None":
            break
        curr = Node(int(item))
        prev.next = curr
        prev = curr

    return head.next
