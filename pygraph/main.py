from pygraph.graph import Graph

def main():
    print("\n--- Undirected Graph Demonstration ---")
    # Create an undirected graph
    undirected_graph = Graph(is_directed=False)

    print("\n--- Adding Nodes to Undirected Graph ---")
    undirected_graph.add_node('A')
    undirected_graph.add_node('B')
    undirected_graph.add_node('C')
    undirected_graph.add_node('D')

    print("\n--- Adding Edges to Undirected Graph ---")
    undirected_graph.add_edge('A', 'B', weight=5)
    undirected_graph.add_edge('B', 'C', weight=2)
    undirected_graph.add_edge('A', 'D', weight=8)
    undirected_graph.add_edge('C', 'D', weight=3)

    print("\n--- Undirected Graph (Text) ---")
    undirected_graph.print_graph_text()

    print("\n--- Undirected Graph (GUI) ---")
    undirected_graph.print_graph_tkinter_gui()

    print("\n--- Directed Graph Demonstration ---")
    # Create a directed graph
    directed_graph = Graph(is_directed=True)

    print("\n--- Adding Nodes to Directed Graph ---")
    directed_graph.add_node('X')
    directed_graph.add_node('Y')
    directed_graph.add_node('Z')

    print("\n--- Adding Edges to Directed Graph ---")
    directed_graph.add_edge('X', 'Y', weight=10) # X -> Y
    directed_graph.add_edge('Y', 'Z', weight=4)  # Y -> Z
    directed_graph.add_edge('Z', 'X', weight=7)  # Z -> X

    print("\n--- Directed Graph (Text) ---")
    directed_graph.print_graph_text()

    print("\n--- Directed Graph (GUI) ---")
    directed_graph.print_graph_tkinter_gui()

if __name__ == "__main__":
    main()