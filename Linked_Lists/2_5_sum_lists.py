# you have two numbers represented by a linked list, where each node contains a single digit.
# the digits are stored in reverse order, such that the 1's digit is at the head of the list.
# write a function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input ( 7 -> 1 -> 6) + ( 5 -> 9 -> 2). That is 617 + 295
# Output: 2 -> 1 -> 9. That is 912
# Suppose the digits are stored in forward order. Repeat the above problem
# Example
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5). That is, 617 + 295.
# Output: (9 -> 1 -> 2). That is 912

from linked_list import LinkedList, Node


def sum_linked_lists(list_one, list_two):
    list_one_values = list()
    list_two_values = list()

    while list_one is not None and list_one.data is not None:
        list_one_values.append(str(list_one.data))
        list_one = list_one.next

    while list_two is not None and list_two.data is not None:
        list_two_values.append(str(list_two.data))
        list_two = list_two.next

    list_one_values.reverse()
    list_two_values.reverse()

    list_one_number = ''.join(list_one_values)
    list_two_number = ''.join(list_two_values)

    total = str(eval('%s + %s' % (list_one_number, list_two_number)))
    total_linked_list = None
    for digit in total:
        head = Node(data=digit, next=total_linked_list)
        total_linked_list = head

    results = LinkedList(head=total_linked_list)
    results.print_linked_list()


def sum_linked_lists_forward_order(list_one, list_two):
    list_one_values = list()
    list_two_values = list()

    while list_one is not None and list_one.data is not None:
        list_one_values.append(str(list_one.data))
        list_one = list_one.next

    while list_two is not None and list_two.data is not None:
        list_two_values.append(str(list_two.data))
        list_two = list_two.next

    list_one_number = ''.join(list_one_values)
    list_two_number = ''.join(list_two_values)

    total = str(eval('%s + %s' % (list_one_number, list_two_number)))
    total_linked_list = None

    index = len(total) - 1
    while index >= 0:
        new_head = Node(data=total[index], next=total_linked_list)
        total_linked_list = new_head
        index -= 1

    result = LinkedList(head=total_linked_list)
    result.print_linked_list()


if __name__ == '__main__':
    list_one = LinkedList(head=Node(data=7, next=None))
    list_one.add_node(1)
    list_one.add_node(6)

    list_two = LinkedList(head=Node(data=5, next=None))
    list_two.add_node(9)
    list_two.add_node(2)

    sum_linked_lists(list_one.head, list_two.head)

    list_one = LinkedList(head=Node(data=6, next=None))
    list_one.add_node(1)
    list_one.add_node(7)

    list_two = LinkedList(head=Node(data=2, next=None))
    list_two.add_node(9)
    list_two.add_node(5)

    sum_linked_lists_forward_order(list_one.head, list_two.head)
