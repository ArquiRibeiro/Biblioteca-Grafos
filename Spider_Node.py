class Node:
    def __init__(self, label, weight=0):
        self.label = label
        self.weight = weight
        self.adjacencyList = dict() #{node : edge}
        #print("Vertice {} criado!".format(self.label))

    def connect(self, node, edge):
        self.adjacencyList.update({node : edge})
        #print("{} foi conectado com {}!".format(self.label, node.label))

    def disconnect(self, node):
        self.adjacencyList.pop(node)
        #print("{} desconectado de {}".format(self.label, node.label))