# tests/test_factory.py
"""
Unit tests for the Tree factory.
"""
import unittest
from pytree import Tree
from pytree.trees.binary_tree import _BinaryTree
from pytree.trees.bst import _BST

class TestTreeFactory(unittest.TestCase):

    def test_create_binary_tree(self):
        """Test that the factory creates a Binary Tree by default."""
        tree = Tree()
        self.assertIsInstance(tree, _BinaryTree)

    def test_create_bst(self):
        """Test that the factory can create a Binary Search Tree."""
        tree = Tree(tree_type='bst')
        self.assertIsInstance(tree, _BST)

    def test_create_with_values(self):
        """Test creating a tree with an initial list of values."""
        values = [10, 5, 15]
        tree = Tree(tree_type='bst', values=values)
        # A simple check to see if the root is correct
        self.assertEqual(tree.root.value, 10)
        self.assertEqual(tree.root.left.value, 5)
        self.assertEqual(tree.root.right.value, 15)

if __name__ == '__main__':
    unittest.main()
