class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    """
    Moves the head node from the source linked list and pushes it onto
    the front of the destination linked list.

    Args:
        source: The head node of the list being pulled from.
        dest: The head node of the list being pushed to.

    Returns:
        Context: An object containing the new head of the source list
                 and the new head of the destination list.

    Raises:
        ValueError: If the source list is empty (None).
    """
    if source is None:
        raise ValueError

    to_move = source.next
    curr = source
    curr.next = dest

    return Context(to_move, curr)
