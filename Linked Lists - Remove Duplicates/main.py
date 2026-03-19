class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    """
    Removes duplicate nodes from a sorted linked list in place.

    Args:
        head: The starting head node of the sorted linked list.

    Returns:
        Node: The head of the modified linked list with all duplicates removed,
              or None if the initial list was empty.
    """
    start = head
    if head is None:
        return

    while head:
        if head.next is None:
            break

        while head.next and head.data == head.next.data:
            head.next = head.next.next

        head = head.next

    return start
