""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    """
    Inserts a new node with the given data into the correct sorted position
    within an ascending sorted linked list.

    Args:
        head: The head node of the sorted linked list.
        data: The integer value to insert into the list.

    Returns:
        Node: The head of the newly updated linked list.
    """
    if head is None:
        return Node(data)

    if data < head.data:
        curr = Node(data)
        curr.next = head
        return curr

    curr = head
    while curr:
        if curr.next is None:
            curr.next = Node(data)
            break

        if curr.data <= data <= curr.next.data:
            tmp = curr.next
            curr.next = Node(data)
            curr.next.next = tmp
            break

        curr = curr.next

    return head
