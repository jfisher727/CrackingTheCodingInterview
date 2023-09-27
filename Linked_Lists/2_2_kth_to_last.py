# Implement an algorithm to find the kth to last element of a singly linked list


from linked_list import Node, LinkedList


def kth_to_last(head, k_to_last):
    flattened_list = list()
    current_node = head

    while current_node is not None:
        flattened_list.append(current_node.data)
        current_node = current_node.next

    return flattened_list[-k_to_last]


if __name__ == '__main__':
    linked_list = LinkedList(head=Node(data=5, next=None))
    linked_list.add_node(18)
    linked_list.add_node(12)
    linked_list.add_node(5)
    linked_list.add_node(32)
    linked_list.add_node(22)
    linked_list.add_node(66)
    linked_list.add_node(18)

    print(kth_to_last(linked_list.head, 3))

