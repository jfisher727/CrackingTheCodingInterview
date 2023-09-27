# write code to partition a linked list around a value x, such that all nodes less than x come before
# all nodes greater than or equal to x. If x i contained within the list, the values of x only need to
# be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right parition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
# output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

from linked_list import Node, LinkedList


def partition_linked_list(head, partition):
    lesser_values = list()
    greater_values = list()

    while head is not None and head.data is not None:
        greater_values.append(head.data) if head.data >= partition else lesser_values.append(head.data)
        head = head.next

    updated_list = LinkedList(head=Node(data=lesser_values[0], next=None))
    for i in range(1, len(lesser_values)):
        updated_list.add_node(lesser_values[i])
    for i in range(0, len(greater_values)):
        updated_list.add_node(greater_values[i])

    updated_list.print_linked_list()


def partition_linked_list_2(head, partition):
    updated_head = None
    updated_tail = None

    while head is not None and head.data is not None:
        if head.data >= partition:
            updated_tail = Node(data=head.data, next=updated_tail)
        else:
            updated_head = Node(data=head.data, next=updated_head)
        head = head.next

    last_node = updated_head
    while last_node.next is not None:
        last_node = last_node.next
    last_node.next = updated_tail

    updated_list = LinkedList(head=updated_head)
    updated_list.print_linked_list()


if __name__ == '__main__':
    linked_list = LinkedList(head=Node(data=3, next=None))
    linked_list.add_node(5)
    linked_list.add_node(8)
    linked_list.add_node(5)
    linked_list.add_node(10)
    linked_list.add_node(2)
    linked_list.add_node(1)

    # partition_linked_list(linked_list.head, 5)
    partition_linked_list_2(linked_list.head, 5)
