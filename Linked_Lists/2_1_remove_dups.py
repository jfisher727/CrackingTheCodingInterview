# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

from linked_list import Node, LinkedList


def remove_dups(head):
    seen_values = set()

    current_node = head
    seen_values.add(current_node.data)
    while current_node is not None and current_node.next is not None:
        pre_add_size = len(seen_values)
        seen_values.add(current_node.next.data)
        post_add_size = len(seen_values)

        if pre_add_size == post_add_size:
            # duplicate value
            current_node.next = current_node.next.next
        current_node = current_node.next

    return head


def remove_dups_no_buffer(head):
    current_node = head
    check_node = head.next

    while current_node is not None and current_node.next is not None:
        pass


if __name__ == '__main__':
    linked_list = LinkedList(head=Node(data=5, next=None))
    linked_list.add_node(18)
    linked_list.add_node(12)
    linked_list.add_node(5)
    linked_list.add_node(32)
    linked_list.add_node(22)
    linked_list.add_node(66)
    linked_list.add_node(18)

    linked_list.head = remove_dups(linked_list.head)
    linked_list.print_linked_list()

