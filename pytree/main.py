# main.py
"""
An example script to demonstrate the usage of the pytree package.

This file shows how to:
- Create a tree from a list of values.
- Add single nodes to an existing tree.
- Print the tree's text-based and GUI representations.
"""

from pytree import Tree

def main():
    """Main function to demonstrate tree creation and visualization."""

    print("--- Binary Search Tree (BST) Demonstration ---")
    # 1. Create a Binary Search Tree from a list
    bst_values = [10, 5, 15, 2, 7, 12, 20]
    print(f"Creating BST from list: {bst_values}")
    bst = Tree(tree_type='bst', values=bst_values)

    # 2. Add a single node
    print("\nAdding a single node (18) to the BST...")
    bst.add(18)

    # 3. Print the text-based representation
    print("\nUpdated BST Structure (Text-based):")
    print(bst)

    # 4. Show the GUI representation
    print("\nLaunching GUI visualization for the BST...")
    # This will open a new window. Close it to continue.
    bst.show_gui()

    print("\nGUI window closed.")
    print("-" * 40)

    print("\n--- Standard Binary Tree Demonstration ---")
    binary_values = [1, 2, 3, 4, 5, 6]
    print(f"Creating Binary Tree from list: {binary_values}")
    binary_tree = Tree(tree_type='binary', values=binary_values)

    print("\nBinary Tree Structure (Text-based):")
    print(binary_tree)

    print("\nLaunching GUI visualization for the Binary Tree...")
    binary_tree.show_gui()
    print("\nGUI window closed.")
    print("-" * 40)


if __name__ == "__main__":
    main()