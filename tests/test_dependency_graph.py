import os
import unittest
from src.dependency_graph import DependencyGraph


class TestDependencyGraph(unittest.TestCase):
    def setUp(self):
        self.graph = DependencyGraph('D:\\Programs\\Graphviz\\bin\\dot.exe', 'D:\\Python\\HomeworkForKU2',
                                     'D:\\Python\\HomeworkForKU2\\output\\output.png')

    def test_build_graph(self):
        self.graph.build_graph()
        with open('graph.dot') as f:
            content = f.read()
            self.assertIn('digraph G {', content)

    def test_run(self):
        self.graph.run()
        self.assertTrue(os.path.exists('D:\\Python\\HomeworkForKU2\\output\\output.png'))


if __name__ == "__main__":
    unittest.main()
