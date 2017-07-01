
from graphviz import Digraph

g = Digraph('g', filename='btree.gv', node_attr={'shape': 'record', 'height': '.1'})

g.node('node0', '<f0> |<f1> G|<f2> ')
g.node('node1', '<f0> |<f1> E|<f2> ')
g.node('node2', '<f0> |<f1> B|<f2> ')
g.node('node3', '<f0> |<f1> F|<f2> ')
g.node('node4', '<f0> |<f1> R|<f2> ')
g.node('node5', '<f0> |<f1> H|<f2> ')
g.node('node6', '<f0> |<f1> Y|<f2> ')
g.node('node7', '<f0> |<f1> A|<f2> ')
g.node('node8', '<f0> |<f1> C|<f2> ')

g.edge('node0:f2', 'node4:f1')
g.edge('node0:f0', 'node1:f1')
g.edge('node1:f0', 'node2:f1')
g.edge('node1:f2', 'node3:f1')
g.edge('node2:f2', 'node8:f1')
g.edge('node2:f0', 'node7:f1')
g.edge('node4:f2', 'node6:f1')
g.edge('node4:f0', 'node5:f1')

g.view()

#arbol.reporteABB()


dot = Digraph(comment='The Round Table')
dot.node('A', 'King Arthur')
dot.node('B', 'Sir Bedevere the Wise')
dot.node('L', 'Sir Lancelot the Brave')
dot.edges(['AB', 'AL'])
dot.edge('B', 'L', constraint='false')
dot.render('test-output/round-table.gv', view=True)