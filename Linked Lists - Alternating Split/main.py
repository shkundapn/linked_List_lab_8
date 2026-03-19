class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    """
    Divides a single linked list into two separate linked lists by alternating nodes.
    Returns a Context object containing the heads of the two new sublists.

    Args:
        head: The starting Node of the original linked list.

    Returns:
        Context: An object containing 'first' and 'second' properties, representing
                 the heads of the two alternating sublists.

    Raises:
        ValueError: If the input list has fewer than two nodes.
    """
    if head is None or head.next is None:
        raise ValueError

    sub1 = Node()
    sub2 = Node()

    p1 = sub1
    p2 = sub2

    current_node = head

    while current_node is not None:
        p1.next = current_node
        p1 = p1.next
        current_node = current_node.next

        if current_node is not None:
            p2.next = current_node
            p2 = p2.next
            current_node = current_node.next

    p1.next = None
    p2.next = None

    return Context(sub1.next, sub2.next)
