class lab1:
    def __init__(self):
        self.connections = {}
    
    def addedge(self, fromNode, toNode, weight):
        if fromNode not in self.connections:
            self.connections[fromNode] = []
        self.connections[fromNode].append((toNode, weight))
    
    def algstart(self, startNode):
        weights = {}
        visited = {}
        prev = {}

        for node in self.connections:
            weights[node] = 1000000
            visited[node] = False
            prev[node] = None
        
        weights[startNode] = 0
        
        for count in range(len(self.connections)):
            minweight = 1000000
            currentNode = None
            
            for node in self.connections:
                if not visited[node] and weights[node] < minweight:
                    minweight = weights[node]
                    currentNode = node
            
            if currentNode is None:
                break
                
            visited[currentNode] = True
            
            if currentNode in self.connections:
                for neighbor, weight in self.connections[currentNode]:
                    if not visited[neighbor]:
                        newweight = weights[currentNode] + weight
                        if newweight < weights[neighbor]:
                            weights[neighbor] = newweight
                            prev[neighbor] = currentNode
        
        return weights, prev
    
    def getpath(self, prev, targetNode):
        path = []
        current = targetNode
        
        while current is not None:
            path.append(current)
            current = prev.get(current)
        
        correctPath = []
        for i in range(len(path)-1, -1, -1):
            correctPath.append(path[i])
        
        return correctPath

def creategraph(Matrix):
    graph = lab1()
    
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            weight = Matrix[i][j]
            if weight > 0:
                graph.addedge(i, j, weight)
    
    return graph

def main():
    Matrix = [
        [0, 4, 2, 0, 0, 0],
        [4, 0, 1, 5, 0, 0],
        [2, 1, 0, 8, 10, 0],
        [0, 5, 8, 0, 2, 6],
        [0, 0, 10, 2, 0, 3],
        [0, 0, 0, 6, 3, 0]
    ]
    
    graph = creategraph(Matrix)
    
    startNode = 0
    weights, prev = graph.algstart(startNode)
    
    print("Кратчайшие расстояния от вершины: ", startNode)
    for node in sorted(weights.keys()):
        weight = weights[node]
        if weight == 1000000:
            print("До", node, ": нет пути")
        else:
            path = graph.getpath(prev, node)
            pathstr = " -> ".join(str(x) for x in path)
            print("До", node, ": ", " есть путь:", pathstr, " Весом: ", weight)

if __name__ == "__main__":
    main()