from PIL import Image
import pydot


class TreePrinting:

    count=0
    def print_tree_console(self, root, prefix="", children_prefix=""):
        if root is None:
            return
        self.count+=1
        children = root.get_successor()
        print(prefix, root)
        for i in range(len(children)):
            if i < len(children) - 1:
                self.print_tree_console(children[i], children_prefix + "├── ", children_prefix + "│   ")
            else:
                self.print_tree_console(children[i], children_prefix + "└── ", children_prefix + "    ")
    def print_count(self):
        print(self.count)

    def print_tree_gui(self, root):
        graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='white')
        stack = [[root, 1]]
        shapes = ['trapezium', 'invtrapezium', 'square']
        colors = ['green', 'blue', 'Yellow']
        graph.add_node(pydot.Node(hash(root), label=root.get_value(), shape=shapes[0], style="filled",
                                  fillcolor=colors[0]))
        while len(stack) > 0:
            node, shape_index = stack.pop()
            children = node.get_successor()
            for child in children:
                stack.append([child, 1 if shape_index == 0 else 0])
                if child.is_pruned():
                    color = 'red'
                else:
                    color = colors[(2 if child.is_leaf() else shape_index)]

                graph.add_node(pydot.Node(hash(child), label=child.get_value(),
                                          shape=shapes[(2 if child.is_leaf() else shape_index)], style="filled",
                                          fillcolor=color))

                edge = pydot.Edge(hash(node), hash(child), label="X" if child.is_pruned() else "")
                graph.add_edge(edge)


        graph.write_png('../assets/test.png')
        img = Image.open('../assets/test.png')
        img.show()

# data to test the tree printer
# root = Node(Node(1))
# root.add_successor(Node(2))
# root.add_successor(Node(3))
# root.add_successor(Node(4))
# root.add_successor(Node(5))
# root.add_successor(Node(6))
# for child in root.get_successor():
#     child.add_successor(Node(7))
#     for c in child.get_successor():
#         c.add_successor(Node(8))
#         c.add_successor(Node(9))
#         c.add_successor(Node(10))
#
#     child.add_successor(Node(8))
#     child.add_successor(Node(9))
#     child.add_successor(Node(10))
#     child.add_successor(Node(11))
#     child.add_successor(Node(12))
#     child.add_successor(Node(13))
#     child.add_successor(Node(14))
#     child.add_successor(Node(15))
#
# p = TreePrinting()
# p.print_tree_console(root, "", "")
# p.print_tree_gui(root)
