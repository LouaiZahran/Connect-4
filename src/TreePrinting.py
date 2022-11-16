from PIL import Image
from Tree import *
import pydot


class TreePrinter:

    def __init__(self):
        pass

    def print_tree_console(self, root, prefix, children_prefix):
        if root is None:
            return

        children = root.get_successor()
        print(prefix, root)
        for i in range(len(children)):
            if i < len(children) - 1:
                self.print_tree_console(children[i], children_prefix + "├── ", children_prefix + "│   ")
            else:
                self.print_tree_console(children[i], children_prefix + "└── ", children_prefix + "    ")

    def print_tree_gui(self, root):
        graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='white')
        stack = [root]
        shapes = ['trapezium', 'invtrapezium', 'square']
        colors = ['green', 'red', 'Yellow']
        shape_index = 0
        graph.add_node(pydot.Node(hash(root), label=root.get_value(), shape=shapes[shape_index], style="filled",
                                  fillcolor=colors[shape_index]))
        while len(stack) > 0:
            shape_index = not shape_index
            node = stack.pop()
            children = node.get_successor()
            for child in children:
                stack.append(child)
                graph.add_node(pydot.Node(hash(child), label=child.get_value(),
                                          shape=shapes[(2 if child.is_leaf() else shape_index)], style="filled",
                                          fillcolor=colors[(2 if child.is_leaf() else shape_index)]))
                edge = pydot.Edge(hash(node), hash(child))
                graph.add_edge(edge)

        graph.write_png('../assets/test.png')
        img = Image.open('../assets/test.png')
        img.show()
        pass


# data to test the tree printer
root = Node(Node(1))
root.add_successor(Node(2))
root.add_successor(Node(3))
root.add_successor(Node(4))
root.add_successor(Node(5))
root.add_successor(Node(6))
for child in root.get_successor():
    child.add_successor(Node(7))
    for c in child.get_successor():
        c.add_successor(Node(8))
        c.add_successor(Node(9))
        c.add_successor(Node(10))

    child.add_successor(Node(8))
    child.add_successor(Node(9))
    child.add_successor(Node(10))
    child.add_successor(Node(11))
    child.add_successor(Node(12))
    child.add_successor(Node(13))
    child.add_successor(Node(14))
    child.add_successor(Node(15))

p = TreePrinter()
p.print_tree_console(root, "", "")
p.print_tree_gui(root)


