import networkx as nx
import random

def generateGraph(vertexCount, edgeProbability):
    graph = nx.Graph()
    graph.add_nodes_from(range(vertexCount))
    
    for i in range(vertexCount):
        for j in range(i + 1, vertexCount):
            if random.random() < edgeProbability:
                graph.add_edge(i, j)
    
    return graph

def calculateAverageDegree(graph):
    degrees = dict(graph.degree())
    return sum(degrees.values()) / graph.number_of_nodes()

def main():
    vertexCount = 100
    edgeProbability = 0.1
    
    graph = generateGraph(vertexCount, edgeProbability)
    
    experimentalAverageDegree = calculateAverageDegree(graph)
    
    theoreticalAverageDegree = (vertexCount - 1) * edgeProbability
    
    print(f"Количество вершин: {vertexCount}")
    print(f"Вероятность ребра: {edgeProbability}")
    print(f"Средняя степень вершины (эксперимент): {experimentalAverageDegree:.4f}")
    print(f"Средняя степень вершины (лекционная): {theoreticalAverageDegree:.4f}")
    print(f"Разница: {abs(experimentalAverageDegree - theoreticalAverageDegree):.4f}")

if __name__ == "__main__":
    main()