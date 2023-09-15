class Node:
    def __init__(self, data, children):
        self.data = data
        self.children = children


def depth_first_search(root, goal):
    visited_nodes = list()
    visited_nodes.append(root)
    while len(visited_nodes) != 0:
        current_node = visited_nodes.pop()
        print(current_node.data)
        if current_node.data == goal:
            return current_node
        current_node.children.reverse()
        for child in current_node.children:
            visited_nodes.append(child)


if __name__ == '__main__':
    root = Node(data='1',
                children=[Node(data='2',
                               children=[Node(data='3',
                                              children=[Node(data='4', children=[]), Node(data='5', children=[])]),
                                         Node(data='6', children=[])]),
                          Node(data='7', children=[]),
                          Node(data='8',
                               children=[Node(data='9',
                                              children=[Node(data='10', children=[]), Node(data='11', children=[])]),
                                         Node(data='12', children=[])]
                               )
                          ]
                )
    print(depth_first_search(root, '12'))
