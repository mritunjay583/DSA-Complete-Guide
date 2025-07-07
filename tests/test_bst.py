# tests/test_bst.py
"""
Unit tests for the _BST (Binary Search Tree) implementation.
"""
import unittest
from pytree import Tree

class TestBST(unittest.TestCase):

    def test_add_to_empty_bst(self):
        """Test adding a node to an empty BST."""
        tree = Tree(tree_type='bst')
        tree.add(10)
        self.assertEqual(tree.root.value, 10)

    def test_add_smaller_node(self):
        """Test that a smaller value is added to the left."""
        tree = Tree(tree_type='bst', values=[10])
        tree.add(5)
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.right)

    def test_add_larger_node(self):
        """Test that a larger value is added to the right."""
        tree = Tree(tree_type='bst', values=[10])
        tree.add(15)
        self.assertEqual(tree.root.right.value, 15)
        self.assertIsNone(tree.root.left)

    def test_add_duplicate_node(self):
        """Test that adding a duplicate value does not change the tree."""
        tree = Tree(tree_type='bst', values=[10, 5])
        tree.add(5) # Add duplicate
        self.assertEqual(tree.root.left.value, 5)
        self.assertIsNone(tree.root.left.left)
        self.assertIsNone(tree.root.left.right)

if __name__ == '__main__':
    unittest.main()
