# implement an algorithm to delete a node in the middle (any node but the first and last node)
# of a singly linked list, given only access to that node.
# EXAMPLE
# input: the node c from the linked list a -> b -> c -> d -> e -> f
# Result: nothing is returned but the new linked list looks like a -> b -> d -> e -> f

def delete_middle(node):
    if node is None or node.next is None:
        # this is the error situation
        return False

    next_node = node.next
    node = next_node.data
    node.next = next_node.next

    return True

