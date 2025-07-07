# pytree/__init__.py
"""
This package provides a simple and extensible way to work with tree data structures.

It uses a factory pattern to create different types of trees (e.g., Binary Tree, BST)
and provides a consistent API for interacting with them.
"""
from typing import Any, List, Literal, Optional

from pytree.trees.binary_tree import _BinaryTree
from pytree.trees.bst import _BST
from pytree.trees.tree_interface import TreeInterface


class Tree:
    """
    A factory class that provides a simple interface for creating and interacting with trees.

    This is the main entry point for the user.
    """

    def __new__(
        cls,
        tree_type: Literal["binary", "bst"] = "binary",
        values: Optional[List[Any]] = None,
    ) -> TreeInterface:
        """
        Creates and returns a specific type of tree instance based on the tree_type.

        This factory method allows for easy extension with new tree types in the future.

        Args:
            tree_type: The type of tree to create ('binary' or 'bst').
            values: An optional list of values to initialize the tree with.

        Returns:
            An instance of the requested tree class that adheres to the TreeInterface.
        """
        if tree_type == "bst":
            tree = _BST()
        else:  # Default to binary tree
            tree = _BinaryTree()

        if values:
            for value in values:
                tree.add(value)

        return tree