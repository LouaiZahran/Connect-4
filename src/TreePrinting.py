import networkx as networkx

import pydot

class TreePrinter:

    def __init__(self):
        pass

    def print_tree_console(self, root, prefix, children_prefix):
        if root is None:
            return

        children = root.get_successor()
        print(prefix, root, "\n")
        for i in range(len(children)):
            if i < len(children)-1:
                self.print_tree_console(children[i], children_prefix + "├── ", children_prefix + "│   ")
            else:
                self.print_tree_console(children[i], children_prefix + "└── ", children_prefix + "    ")


    def print_tree_gui(self, root):
        graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='yellow')
        stack = [root]
        graph.add_node(pydot.Node('a', label='Foo'))
        while len(stack) > 0:
            node = stack.pop()
            children = node.get_successor()
            for child in children:
                stack.append(child)
                edge = pydot.Edge(node, child)
                graph.add_edge(edge)

        graph = networkx.drawing.nx_pydot.to_pydot(graph)
        G = networkx.complete_graph(5)
        networkx.draw(G)
        pass



#
import pydot
import matplotlib.pyplot as plt

graph = pydot.Dot('my_graph', graph_type='graph', bgcolor='yellow')

# Add nodes
my_node = pydot.Node('a', label='Foo')
graph.add_node(my_node)
# Or, without using an intermediate variable:
graph.add_node(pydot.Node('b', shape='circle'))

# Add edges
my_edge = pydot.Edge('a', 'b', color='blue')
graph.add_edge(my_edge)
# Or, without using an intermediate variable:
graph.add_edge(pydot.Edge('b', 'c', color='blue'))
# graph.write_png('output.png')
# As a string:
# output_raw_dot = graph.to_string()
# # Or, save it as a DOT-file:
# graph.write_raw('output_raw.dot')
# G = networkx.complete_graph(graph)
# networkx.draw_shell(G)