# pytree/trees/tree_interface.py
"""
Defines the interface that all tree implementations must follow.
"""
from abc import ABC, abstractmethod
from typing import Any

class TreeInterface(ABC):
    """
    An abstract base class that defines the common methods for all tree types.
    This ensures that different tree implementations can be used interchangeably.
    """

    @abstractmethod
    def add(self, value: Any) -> None:
        """Adds a new node with the given value to the tree."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Returns a string representation of the tree."""
        pass

    @abstractmethod
    def show_gui(self) -> None:
        """Displays the tree in a graphical user interface (GUI)."""
        pass