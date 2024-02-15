class Node:
    def __init__(self,vertex):
        self.neighbour = set()
        self.vertex = vertex
        self.visited = False

    def add_neighbour(self,node):
        self.neighbour.add(node)
    
    def __str__(self):
        string=str(self.vertex)+": "
        string += " ".join([str(i.vertex) for i in self.neighbour])
        return string
    

def dfs(node):
    
    print(node.vertex)
    for i in node.neighbour:
        dfs(i)


def bfs(node):
    
    queue = []
    queue.append(node)
    while len(queue)!=0:
        a = queue.pop(0)
        a.visited = True
        print(a)
        for i in a.neighbour:
            if (i in queue)==False and i.visited == False:
                queue.append(i)
            

if __name__=="__main__":
    graph = []
    for i in range(8):
        graph.append(Node(i))

    graph[0].add_neighbour(graph[1])
    graph[0].add_neighbour(graph[4])
    graph[1].add_neighbour(graph[2])
    graph[1].add_neighbour(graph[3])
    graph[4].add_neighbour(graph[5])
    graph[5].add_neighbour(graph[6])

    print("DFS:")
    dfs(graph[0])

    print("BFS:")
    bfs(graph[0])