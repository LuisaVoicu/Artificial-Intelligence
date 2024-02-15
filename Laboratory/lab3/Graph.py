import Node

class Graph():
    def __init__(self, nb_nodes, nodes):
        self.nb_nodes = nb_nodes
        self.nodes = nodes

    def add_edge(self, n1, n2):
        self.nodes[n1].edge(nodes[n2])


    def print_graph(self):
        for i in range(self.nb_nodes + 1):
            nodes[i].printNeighbours()

    def out_degree(self, node):
        return len(nodes[node].neighbours)




nodes = []
for i in range(7):
    nodes.append(Node.Node(i))

f = open(r'graph1.txt')


nb_nodes = int(f.readline())
graph = Graph(nb_nodes, nodes)

for line in f:
    node = line.split(" ")
    nb1 = int(node[0])
    nb2 = int(node[1])
    print("my nnb are: ", nb1, "  " ,nb2)
    graph.add_edge(nb1,nb2)

graph.print_graph()

print("out degrees: ")
for i in range(nb_nodes + 1):
    print(i, " : ", graph.out_degree(i))
