class Edge:
    def __init__(self, nodes, label="", weight=0, directed=False):
        self.nodes = nodes
        self.label = label        
        self.weight = weight
        self.directed = directed