import numpy 

class Node():

    def __init__(self, vertex_number):
        self.vertex_number = vertex_number
        self.neighbours = []

    def edge(self, node):
        self.neighbours.append(node)

    def printNeighbours(self):
        str_result = "" 
        for i in self.neighbours:
            str_result +=  str(i) + " "
        print(self.vertex_number, " : " , str_result)

    def __str__(self):
        return f'({self.vertex_number})'

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
    
    def get_null_matrix(self):
        line = []
        for i in range(self.nb_nodes+1):
            line.append(0)
        matrix_list = [] 
        for i in range(self.nb_nodes+1):
            matrix_list.append(line)
        
        return numpy.array(matrix_list)
    
    def get_adjacency_matrix(self):
        matrix = self.get_null_matrix()
        for i in range(self.nb_nodes+1):
            for neighbour in self.nodes[i].neighbours:
                matrix[i,neighbour.vertex_number]=1
        return matrix



    




nodes = []
for i in range(7):
    nodes.append(Node(i))

f = open(r'ex7.txt')


nb_nodes = int(f.readline())
graph = Graph(nb_nodes, nodes)

for line in f:
    node = line.split(" ")
    nb1 = int(node[0])
    nb2 = int(node[1])
    graph.add_edge(nb1,nb2)

# graph.print_graph()

print("out degrees: ")
for i in range(nb_nodes + 1):
    print(i, " : ", graph.out_degree(i))
matrix = graph.get_adjacency_matrix()
print(matrix)