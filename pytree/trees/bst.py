# pytree/trees/bst.py
"""
This module provides the implementation of a Binary Search Tree (BST).
"""
from typing import Any, Optional

from pytree.node import Node
from pytree.trees.tree_interface import TreeInterface
from pytree.trees.binary_tree import _BinaryTree

class _BST(_BinaryTree):
    """
    Implements a Binary Search Tree (BST).

    Inherits from _BinaryTree but overrides the 'add' method to ensure
    the BST property is maintained (left child < parent < right child).

    This class is intended for internal use by the TreeFactory.
    """
    def add(self, value: Any) -> None:
        """
        Adds a new node to the BST based on its value.

        Args:
            value: The value to add. Smaller values go to the left, larger to the right.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current: Node, value: Any) -> None:
        """Helper method to recursively find the correct position for the new node."""
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._add_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._add_recursive(current.right, value)
        # If value is equal, do nothing (or handle as per specific requirements)
