class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    """
    Reverses a singly linked list using a recursive approach.

    Args:
        head: The starting head node of the linked list.

    Returns:
        Node: The new head of the completely reversed linked list.
    """
    if head is None or head.next is None:
        return head

    val = reverse(head.next)
    head.next.next = head
    head.next = None

    return val
