# tests/test_binary_tree.py
"""
Unit tests for the _BinaryTree implementation.
"""
import unittest
from pytree import Tree

class TestBinaryTree(unittest.TestCase):

    def test_add_to_empty_tree(self):
        """Test adding a node to an empty binary tree."""
        tree = Tree()
        tree.add(1)
        self.assertEqual(tree.root.value, 1)

    def test_add_multiple_nodes(self):
        """Test the level-order insertion of multiple nodes."""
        tree = Tree()
        nodes = [1, 2, 3, 4]
        for node in nodes:
            tree.add(node)
        
        self.assertEqual(tree.root.value, 1)
        self.assertEqual(tree.root.left.value, 2)
        self.assertEqual(tree.root.right.value, 3)
        self.assertEqual(tree.root.left.left.value, 4)

if __name__ == '__main__':
    unittest.main()
