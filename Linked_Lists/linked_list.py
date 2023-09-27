class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head

    def add_node(self, data):
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next

        new_node = Node(data, None)
        current_node.next = new_node

    def remove_node(self, data):
        current_node = self.head

        if current_node.data == data:
            self.head = current_node.next

        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
            current_node = current_node.next

    def print_linked_list(self):
        current_node = self.head
        print(current_node.data)
        while current_node.next is not None:
            print(current_node.next.data)
            current_node = current_node.next
