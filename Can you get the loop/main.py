def loop_size(node):
    """
    Determines the length of a loop in a linked list using Floyd's Cycle Detection
    (Tortoise and Hare algorithm) to ensure O(1) space complexity.

    Args:
        node: The starting head node of the linked list.

    Returns:
        int: The number of nodes that make up the loop. Returns 0 if no loop exists.
    """
    slow = node
    fast = node
    flag = 0
    index = 0

    while True:
        try:
            fast = fast.next.next
        except Exception:
            break

        slow = slow.next

        if fast == slow:
            flag = 1
            break

    if not flag:
        return 0

    while True:
        fast = fast.next
        index += 1
        if fast == slow:
            break

    return index
