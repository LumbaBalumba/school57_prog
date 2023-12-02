def empty(node):
    return len(node) == 0

def add_elem(node, elem):
    if empty(node):
        node.append(elem)
        node.append([])
        node.append([])
    elif elem > node[0]:
        if empty(node[2]):
            node[2] = [elem, [], []]
        else:
            add_elem(node[2], elem)
    else:
        if empty(node[1]):
            node[1] = [elem, [], []]
        else:
            add_elem(node[1], elem)


class Node:
    value: float
    left
    right

    def __init__(self, value):
        self.value = value
        self.left = self.right = None

#    def empty(self):
#        return self.value is None and self.left is None and self.right is None

    def add(self, elem):
        if elem > self.value:
            if self.right is None:
                 self.right = Node(elem)
            else: 
                 self.right.add(elem)
        else:
            if self.left is None:
                self.left = Node(elem)
            else:
                self.left.add(elem)
