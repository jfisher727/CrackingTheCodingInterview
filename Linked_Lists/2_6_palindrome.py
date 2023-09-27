# Implement an algorithm to check if a linked list is a palindrome

from linked_list import LinkedList, Node


def palindrome_check(head):
    values = list()
    while head is not None and head.data is not None:
        values.append(head.data)
        head = head.next

    palindrome_found = True
    for index in range(0, int(len(values) / 2)):
        if values[index] != values[len(values) - index - 1]:
            palindrome_found = False

    return palindrome_found


if __name__ == '__main__':
    palindrome = LinkedList(head=Node(data='r', next=None))
    palindrome.add_node('a')
    palindrome.add_node('c')
    palindrome.add_node('e')
    palindrome.add_node('c')
    palindrome.add_node('a')
    palindrome.add_node('r')

    not_palindrome = LinkedList(head=Node(data='c', next=None))
    not_palindrome.add_node('o')
    not_palindrome.add_node('d')
    not_palindrome.add_node('i')
    not_palindrome.add_node('n')
    not_palindrome.add_node('g')

    print(palindrome_check(palindrome.head))
    print(palindrome_check(not_palindrome.head))
