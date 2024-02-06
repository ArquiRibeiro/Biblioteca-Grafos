import unittest
import Spider as sp

class GraphTest(unittest.TestCase):
    def setUp(self):
        self.testGraph1 = sp.Graph()
        self.testGraph2 = sp.Graph(nodes=3)

    def testGraphWithThreeNodes(self):
        self.assertEqual(len(self.testGraph2.nodes), 3)

    def testGraphCountNodes(self):
        self.assertEqual(self.testGraph1.countNodes(), 0)
        self.assertEqual(self.testGraph2.countNodes(), 3)

    def testRemoveEdges(self):
        self.assertEqual(self.testGraph2.countEdges(), 0)
        self.testGraph2.addEdge(node1="A", node2="B")
        self.assertEqual(self.testGraph2.countEdges(), 1)

    def testDijkstra(self):
        print("")
        
        testGraph3 = sp.Graph(6)
        testGraph3.addEdge("A", "B", weight=1)
        testGraph3.addEdge("A", "C", weight=1)
        testGraph3.addEdge("A", "E", weight=4)
        testGraph3.addEdge("B", "D", weight=3)
        testGraph3.addEdge("B", "E", weight=1)
        testGraph3.addEdge("C", "E", weight=2)
        testGraph3.addEdge("C", "F", weight=3)
        testGraph3.addEdge("D", "E", weight=1)
        testGraph3.addEdge("E", "F", weight=2)

        testGraph3.exportAsPajekDotNet("./Pajek_Dijkstra_slides.net")

        print(testGraph3.printAdjacencyList())
        if testGraph3.dijkstra("A"):
            print("Dijkstra sucedido!")
    
    def testBellmanFord(self):
        print("")
        testGraph3 = sp.Graph(7)

        testGraph3.addEdge("A", "B", weight=6, directed=True)
        testGraph3.addEdge("A", "C", weight=5, directed=True)
        testGraph3.addEdge("A", "D", weight=5, directed=True)
        testGraph3.addEdge("B", "E", weight=-1, directed=True)
        testGraph3.addEdge("C", "B", weight=-2, directed=True)
        testGraph3.addEdge("C", "E", weight=1, directed=True)
        testGraph3.addEdge("D", "C", weight=-2, directed=True)
        testGraph3.addEdge("D", "F", weight=-1, directed=True)
        testGraph3.addEdge("E", "G", weight=3, directed=True)
        testGraph3.addEdge("F", "G", weight=3, directed=True)

        testGraph3.exportAsPajekDotNet("./Pajek_BellmanFord_slides.net")
        
        print(testGraph3.printAdjacencyList())
        if testGraph3.bellmanFord("A"):
            print("Bellman-Ford sucedido!")

if __name__ == '__main__':
    unittest.main()