class Node:
    def __init__(self, value):
        self.value = value
        self.successor = []
        self.pruned = False

    def __str__(self):
        return str(self.value)

    def add_successor(self, node):
        self.successor.append(node)

    def get_successor(self):
        return self.successor

    def get_value(self):
        return self.value

    def is_leaf(self):
        return len(self.successor) == 0

    def is_pruned(self):
        return self.pruned


# class Tree:
#     def __init__(self, node):
#         self.root = node
#
#     def get_root(self):
#         return self.root
#
#     def set_root(self, node):
#         self.root = node
