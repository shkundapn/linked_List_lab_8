from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    lst = list_repr.split(" -> ")
    head = prev =  Node(0)
    for i , item in enumerate(lst):
        if item == "None":
            break
        curr = Node(int(item) )
        prev.next = curr
        prev = curr


    return head.next
