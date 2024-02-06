import sys
import Spider_Node as spn
import Spider_Edge as spe

class Graph:    
    def __init__(self, nodes=0, numericSetupNodes=False, complete=False):
        self.nodes = dict()
        self.edges = dict()
        self.nodePositionsByLabel = dict()

        self.defaultEdgeCounter = 1

        if numericSetupNodes == False:
            for i in range (0, nodes):
                label=chr(65 + i)
                self.addNode(label)
        else:
            for i in range (0, nodes):
                self.addNode(label=str(i+1))
        
        if complete==True:
            for index, node in enumerate(self.nodes):
                for node2 in list(self.nodes.keys())[index+1:]:
                    self.addEdge(node, node2, directed=True)
        
        return

    def countNodes(self):
        return len(self.nodes)
    
    def addNode(self, label, weight=0):
        self.nodes.update({label : spn.Node(label=label)})

        return
            
    def countEdges(self):
        return len(self.edges)
    
    def addEdge(self, node1, node2, label="Untitled", weight=0, directed=False):
        if label == "Untitled":
            label = "Aresta{}".format(self.defaultEdgeCounter)
            self.defaultEdgeCounter += 1
        
        node1 = self.nodes[node1]
        node2 = self.nodes[node2]

        edge = spe.Edge([node1, node2], label=label, weight=weight, directed=directed)

        node1.connect(node2, edge)

        if directed == False:
            node2.connect(node1, edge)
        
        #self.edges.update({"{}-{}".format(node1.label, node2.label) : edge})
        self.edges.update({label : edge})

        return

    def removeEdge(self, edge):
        edge = self.edges[edge]
        nodes = edge.nodes

        nodes[0].disconnect(nodes[1])
        nodes[1].disconnect(nodes[0])

        self.edges.pop(edge.label)
        
        #self.adjacencyList.update({nodes[0] : list(nodes[0].adjacencyList.keys())})
        #self.adjacencyList.update({nodes[1] : list(nodes[1].adjacencyList.keys())})

        return

    def printEdges(self):
        print("#ARESTAS ({}):".format(self.countEdges()))
        if not self.isEmpty() > 0:
            for edge in self.edges:
                edge = self.edges[edge]
                print("\t- {} ({}-{}, {})".format(edge.label, edge.nodes[0].label, edge.nodes[1].label, edge.weight))
            return
        
        print("\t(Sem arestas)")
    
    def printAdjacencyList(self):
        # for i in self.adjacencyList:
        #     print("{}:\t[".format(i.label), end="")
        #     for j in self.adjacencyList[i]:
        #         print(j.label, end="")
        #     print("]")

        # print("!!!TESTEEEE: {}".format(self.nodes["A"].adjacencyList))

        for node in self.nodes:
            print("{}: \t[".format(node),end="")
            for node1 in self.nodes[node].adjacencyList:
                print(node1.label,end="")

            print("]")

        return

    #def updateDjacencyList(self):
    
    def adjacencyBetweenNodes(self, node1, node2):
        node1 = self.nodes[node1]
        node2 = self.nodes[node2]
        
        if node2 in node1.adjacencyList:
            return True
        
        return False
    
    def incidence(self, node, edge):
        node = self.nodes[node]
        edge = self.edges[edge]

        if node in edge.nodes:                
                return True
            
        return False

    def isEmpty(self):
        if len(self.edges) > 0:
            return False
        
        return True
    
    def isComplete(self):
        nodesCount = len(self.nodes)
        edgesCount = len(self.edges)
        
        if edgesCount == (nodesCount * (nodesCount-1))/2:
            return True
        
        return False
    
    def exportAsPajekDotNet(self, filePath):
        f = open(filePath, "w")
        pajekString = "*vertices {}\n".format(self.countNodes()) #qual a diferença de arcs para edges? (pagina 92 de Pajekman.pdf)
        for index, node in enumerate(self.nodes):
            pajekString += "\t{} \"{}\"\n".format(index+1, self.nodes[node].label)

        
        pajekString += "*arcs\n"
        for edge in self.edges:
            pajekString += "\t{} {} {}\n".format(self.edges[edge].nodes[0].label, self.edges[edge].nodes[1].label, self.edges[edge].weight)
        
        f.write(pajekString)
        f.close()

    def dijkstra(self, startNode):
        startNode = self.nodes[startNode]
        notVisited = list()
        distances= dict()

        for node in self.nodes:
            notVisited.append(self.nodes[node])
            distances.update({self.nodes[node] : sys.maxsize})
        
        #notVisited.append(startNode)
        distances[startNode] = 0
        selectedNode = startNode
        notVisited.remove(selectedNode)
        
        while len(notVisited) != 0:
            for node2 in selectedNode.adjacencyList:
                #notVisited.append(node2)
                #print(selectedNode.adjacencyList[node2].weight)
                if(distances[selectedNode] + selectedNode.adjacencyList[node2].weight < distances[node2]):
                    distances[node2] = distances[selectedNode] + selectedNode.adjacencyList[node2].weight
            
            selectedNode = notVisited[0]
            notVisited.remove(selectedNode)
            
            for node in notVisited:
                if distances[node] < distances[selectedNode]:
                    selectedNode = node

        for node in distances:
            print("{} - {}".format(node.label, distances[node]))

        return distances

    def dijkstraAll(self):
        for node in self.nodes:
            print("Node: {}".format(node))
            self.dijkstra(node)
    
    def bellmanFord(self, startNode):
        pathUpdated = True
        distances= dict()

        for node in self.nodes:
            distances.update({self.nodes[node] : sys.maxsize})
        
        distances[self.nodes[startNode]] = 0
        for _ in range(len(self.nodes) -1):
            for edge in self.edges:
                edge = self.edges[edge]
                #print("U:{} V:{} W:{}".format(edge.nodes[0].label,edge.nodes[1].label,edge.weight))
                #print(distances.values())
                if distances[edge.nodes[0]] != sys.maxsize and distances[edge.nodes[0]] + edge.weight < distances[edge.nodes[1]]:
                    distances[edge.nodes[1]] = distances[edge.nodes[0]] + edge.weight
        
        for node in distances:
            print("{} - {}".format(node.label, distances[node]))
        
        return distances
    
    def bellmanFordAll(self):
        for node in self.nodes:
            print("Node: {}".format(node))
            self.bellmanFord(node)

    