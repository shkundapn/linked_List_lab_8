from preloaded import Node

def swap_pairs(head):
    """
    Swaps every two adjacent nodes in a linked list and returns its new head.
    Uses a dummy node to handle edge cases and iteratively re-routes pointers
    in O(n) time and O(1) space.

    Args:
        head: The starting node of the linked list.

    Returns:
        Node: The new head of the modified linked list after swapping pairs.
    """
    start = Node(0)
    start.next = head

    prev = start
    curr = head

    while curr and curr.next:
        second = curr.next
        next_pair = curr.next.next

        second.next = curr
        curr.next = next_pair
        prev.next = second

        prev = curr
        curr = next_pair

    return start.next
