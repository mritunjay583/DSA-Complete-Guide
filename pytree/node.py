# pytree/node.py
"""
This module defines the basic Node class, which is a building block for tree structures.
"""
from typing import Any, Optional

class Node:
    """
    Represents a single node in a tree.

    Attributes:
        value: The data stored in the node.
        left (Optional[Node]): A reference to the left child node.
        right (Optional[Node]): A reference to the right child node.
    """
    def __init__(self, value: Any):
        self.value = value
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None
