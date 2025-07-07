# pytree/trees/binary_tree.py
"""
This module provides the implementation of a standard Binary Tree.
"""
from collections import deque
from typing import Any, Optional

from pytree.node import Node
from pytree.trees.tree_interface import TreeInterface

class _BinaryTree(TreeInterface):
    """
    Implements a standard Binary Tree where nodes are added in level order.

    This class is intended for internal use by the TreeFactory.
    """
    def __init__(self):
        self.root: Optional[Node] = None

    def add(self, value: Any) -> None:
        """
        Adds a new node to the tree in the first available position (level order).

        Args:
            value: The value to add to the tree.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            nodes = deque([self.root])
            while nodes:
                current = nodes.popleft()
                if current.left is None:
                    current.left = Node(value)
                    return
                if current.right is None:
                    current.right = Node(value)
                    return
                nodes.append(current.left)
                nodes.append(current.right)

    def __str__(self) -> str:
        """Delegates the string representation to the visualizer."""
        from pytree.visualizer import Visualizer
        return Visualizer.get_tree_string(self.root)

    def show_gui(self) -> None:
        """Delegates the GUI visualization to the visualizer."""
        from pytree.visualizer import GUIVisualizer
        gui = GUIVisualizer(self.root)
        gui.show()
