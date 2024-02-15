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

