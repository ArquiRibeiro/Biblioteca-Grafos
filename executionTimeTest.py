import time
import Spider as sp

graphs = list()
graphs.append(sp.Graph(5, numericSetupNodes=True ,complete=True))
graphs.append(sp.Graph(50, numericSetupNodes=True ,complete=True))
graphs.append(sp.Graph(500, numericSetupNodes=True ,complete=True))

print("#Dijkstra")
for graph in graphs:
    start = time.time()

    graph.dijkstra("1")

    end = time.time()

    print("Tempo de execucao com {} vertices:\t{}ms".format(graph.countNodes(),(end-start) * 10**3))

print("\n#Bellman-Ford")
for graph in graphs:
    start = time.time()

    graph.bellmanFord("1")

    end = time.time()

    print("Tempo de execucao com {} vertices:\t{}ms".format(graph.countNodes(),(end-start) * 10**3))
