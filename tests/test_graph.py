import unittest
from pygraph.graph import Graph

class TestGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

    def test_add_node(self):
        self.graph.add_node('A')
        self.assertIn('A', self.graph.nodes)
        self.assertIn('A', self.graph.adj_list)
        self.assertEqual(len(self.graph.adj_matrix), 1)
        self.assertEqual(len(self.graph.adj_matrix[0]), 1)

        self.graph.add_node('B')
        self.assertIn('B', self.graph.nodes)
        self.assertIn('B', self.graph.adj_list)
        self.assertEqual(len(self.graph.adj_matrix), 2)
        self.assertEqual(len(self.graph.adj_matrix[0]), 2)
        self.assertEqual(len(self.graph.adj_matrix[1]), 2)

        # Test adding existing node
        self.graph.add_node('A')
        self.assertEqual(len(self.graph.nodes), 2)

    def test_delete_node(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')

        self.graph.delete_node('B')
        self.assertNotIn('B', self.graph.nodes)
        self.assertNotIn('B', self.graph.adj_list)
        self.assertEqual(len(self.graph.adj_matrix), 2)
        self.assertEqual(len(self.graph.adj_matrix[0]), 2)

        # Check adj_list integrity
        self.assertNotIn('B', self.graph.adj_list.get('A', []))
        self.assertNotIn('B', self.graph.adj_list.get('C', []))

        # Check adj_matrix integrity (A and C should still be connected if they were)
        # In this case, A and C were not directly connected, so matrix should reflect that
        idx_a = self.graph._node_to_index.get('A')
        idx_c = self.graph._node_to_index.get('C')
        if idx_a is not None and idx_c is not None:
            self.assertEqual(self.graph.adj_matrix[idx_a][idx_c], 0)
            self.assertEqual(self.graph.adj_matrix[idx_c][idx_a], 0)

        # Test deleting non-existent node
        self.graph.delete_node('D')
        self.assertEqual(len(self.graph.nodes), 2)

    def test_add_edge(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')

        self.graph.add_edge('A', 'B')
        self.assertIn('B', self.graph.adj_list['A'])
        self.assertIn('A', self.graph.adj_list['B'])
        idx_a = self.graph._node_to_index['A']
        idx_b = self.graph._node_to_index['B']
        self.assertEqual(self.graph.adj_matrix[idx_a][idx_b], 1)
        self.assertEqual(self.graph.adj_matrix[idx_b][idx_a], 1)

        self.graph.add_edge('B', 'C', weight=5)
        self.assertIn('C', self.graph.adj_list['B'])
        self.assertIn('B', self.graph.adj_list['C'])
        idx_b = self.graph._node_to_index['B']
        idx_c = self.graph._node_to_index['C']
        self.assertEqual(self.graph.adj_matrix[idx_b][idx_c], 5)
        self.assertEqual(self.graph.adj_matrix[idx_c][idx_b], 5)

        # Test adding edge with non-existent node
        self.graph.add_edge('A', 'D')
        self.assertNotIn('D', self.graph.adj_list['A'])

    def test_delete_edge(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_node('C')
        self.graph.add_edge('A', 'B')
        self.graph.add_edge('B', 'C')

        self.graph.delete_edge('A', 'B')
        self.assertNotIn('B', self.graph.adj_list['A'])
        self.assertNotIn('A', self.graph.adj_list['B'])
        idx_a = self.graph._node_to_index['A']
        idx_b = self.graph._node_to_index['B']
        self.assertEqual(self.graph.adj_matrix[idx_a][idx_b], 0)
        self.assertEqual(self.graph.adj_matrix[idx_b][idx_a], 0)

        # Test deleting non-existent edge
        self.graph.delete_edge('A', 'C')
        self.assertNotIn('C', self.graph.adj_list['A'])

    def test_print_graph_text(self):
        self.graph.add_node('A')
        self.graph.add_node('B')
        self.graph.add_edge('A', 'B')

        # This test primarily checks if the method runs without error and produces some output.
        # More robust testing would involve capturing stdout and asserting its content.
        try:
            self.graph.print_graph_text()
        except Exception as e:
            self.fail(f"print_graph_text raised an exception: {e}")

    def test_print_graph_tkinter_gui(self):
        self.graph.add_node('X')
        self.graph.add_node('Y')
        self.graph.add_edge('X', 'Y', weight=10)

        try:
            # This test primarily checks if the method runs without error.
            # Actual visual verification would require manual inspection.
            self.graph.print_graph_tkinter_gui()
        except Exception as e:
            self.fail(f"print_graph_tkinter_gui raised an exception: {e}")

    def test_directed_graph_add_edge(self):
        directed_graph = Graph(is_directed=True)
        directed_graph.add_node('A')
        directed_graph.add_node('B')
        directed_graph.add_edge('A', 'B')

        self.assertIn('B', directed_graph.adj_list['A'])
        self.assertNotIn('A', directed_graph.adj_list['B'])
        idx_a = directed_graph._node_to_index['A']
        idx_b = directed_graph._node_to_index['B']
        self.assertEqual(directed_graph.adj_matrix[idx_a][idx_b], 1)
        self.assertEqual(directed_graph.adj_matrix[idx_b][idx_a], 0)

    def test_directed_graph_delete_edge(self):
        directed_graph = Graph(is_directed=True)
        directed_graph.add_node('A')
        directed_graph.add_node('B')
        directed_graph.add_edge('A', 'B')
        directed_graph.delete_edge('A', 'B')

        self.assertNotIn('B', directed_graph.adj_list['A'])
        self.assertNotIn('A', directed_graph.adj_list['B'])
        idx_a = directed_graph._node_to_index['A']
        idx_b = directed_graph._node_to_index['B']
        self.assertEqual(directed_graph.adj_matrix[idx_a][idx_b], 0)
        self.assertEqual(directed_graph.adj_matrix[idx_b][idx_a], 0)

if __name__ == '__main__':
    unittest.main()
