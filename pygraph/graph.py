

class Graph:
    def __init__(self, is_directed=False):
        self.nodes = []
        self.adj_list = {}
        self.adj_matrix = []
        self._node_to_index = {}
        self._next_index = 0
        self.is_directed = is_directed

    def add_node(self, node_id):
        if node_id in self.nodes:
            print(f"Node {node_id} already exists.")
            return

        self.nodes.append(node_id)
        self.adj_list[node_id] = []
        self._node_to_index[node_id] = self._next_index
        self._next_index += 1

        # Update adjacency matrix
        for row in self.adj_matrix:
            row.append(0)  # Add new column
        self.adj_matrix.append([0] * len(self.nodes))  # Add new row

        print(f"Node {node_id} added.")

    def delete_node(self, node_id):
        if node_id not in self.nodes:
            print(f"Node {node_id} does not exist.")
            return

        index_to_remove = self._node_to_index[node_id]

        # Remove from nodes list
        self.nodes.remove(node_id)

        # Remove from adjacency list
        del self.adj_list[node_id]
        for node in self.adj_list:
            self.adj_list[node] = [n for n in self.adj_list[node] if n != node_id]

        # Rebuild _node_to_index
        self._node_to_index = {node: i for i, node in enumerate(self.nodes)}
        self._next_index = len(self.nodes)

        # Rebuild adjacency matrix
        new_adj_matrix = []
        for i, row in enumerate(self.adj_matrix):
            if i == index_to_remove:
                continue
            new_row = []
            for j, val in enumerate(row):
                if j == index_to_remove:
                    continue
                new_row.append(val)
            if new_row:
                new_adj_matrix.append(new_row)
        self.adj_matrix = new_adj_matrix

        print(f"Node {node_id} deleted.")

    def add_edge(self, node1_id, node2_id, weight=1):
        if node1_id not in self.nodes or node2_id not in self.nodes:
            print("One or both nodes not found.")
            return

        if node2_id not in self.adj_list[node1_id]:
            self.adj_list[node1_id].append(node2_id)

        idx1 = self._node_to_index[node1_id]
        idx2 = self._node_to_index[node2_id]
        self.adj_matrix[idx1][idx2] = weight

        if not self.is_directed:
            if node1_id not in self.adj_list[node2_id]:
                self.adj_list[node2_id].append(node1_id)
            self.adj_matrix[idx2][idx1] = weight

        print(f"Edge between {node1_id} and {node2_id} added.")

    def delete_edge(self, node1_id, node2_id):
        if node1_id not in self.nodes or node2_id not in self.nodes:
            print("One or both nodes not found.")
            return

        if node2_id in self.adj_list[node1_id]:
            self.adj_list[node1_id].remove(node2_id)

        idx1 = self._node_to_index[node1_id]
        idx2 = self._node_to_index[node2_id]
        self.adj_matrix[idx1][idx2] = 0

        if not self.is_directed:
            if node1_id in self.adj_list[node2_id]:
                self.adj_list[node2_id].remove(node1_id)
            self.adj_matrix[idx2][idx1] = 0

        print(f"Edge between {node1_id} and {node2_id} deleted.")

    def print_graph_text(self):
        print("\n--- Adjacency List ---")
        for node, neighbors in self.adj_list.items():
            print(f"{node}: {neighbors}")

        print("\n--- Adjacency Matrix ---")
        if not self.nodes:
            print("Graph is empty.")
            return

        # Print header row for matrix
        header = [" "] + [str(node) for node in self.nodes]
        print(" ".join(f"{item:<3}" for item in header))

        for i, node1 in enumerate(self.nodes):
            row_str = [f"{node1:<3}"]
            for j, node2 in enumerate(self.nodes):
                row_str.append(f"{self.adj_matrix[i][j]:<3}")
            print(" ".join(row_str))

    def print_graph_tkinter_gui(self):
        try:
            import tkinter as tk
            import math
        except ImportError:
            print("Tkinter not found. Please ensure you have a Python distribution with Tkinter.")
            return

        if not self.nodes:
            print("Graph is empty. Nothing to display in GUI.")
            return

        self.window = tk.Tk()
        self.window.title("Graph Visualization")

        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.scale = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.last_mouse_x = 0
        self.last_mouse_y = 0

        node_radius = 25
        center_x, center_y = 400, 300  # Adjusted for larger canvas
        graph_radius = 250  # Adjusted for larger canvas

        # Calculate initial node positions in a circular layout
        self.positions = {}
        num_nodes = len(self.nodes)
        if num_nodes > 0:
            for i, node_id in enumerate(self.nodes):
                angle = 2 * math.pi * i / num_nodes
                x = center_x + graph_radius * math.cos(angle)
                y = center_y + graph_radius * math.sin(angle)
                self.positions[node_id] = (x, y)

        def _transform_coords(x, y):
            return (x * self.scale + self.offset_x, y * self.scale + self.offset_y)

        def _draw_elements():
            self.canvas.delete("all")  # Clear canvas

            scaled_node_radius = node_radius * self.scale

            # Draw edges
            for node1_id, neighbors in self.adj_list.items():
                x1_orig, y1_orig = self.positions[node1_id]
                for node2_id in neighbors:
                    x2_orig, y2_orig = self.positions[node2_id]

                    x1, y1 = _transform_coords(x1_orig, y1_orig)
                    x2, y2 = _transform_coords(x2_orig, y2_orig)

                    # Calculate adjusted endpoints for arrow to be outside the node
                    angle = math.atan2(y2 - y1, x2 - x1)
                    adjusted_x2 = x2 - scaled_node_radius * math.cos(angle)
                    adjusted_y2 = y2 - scaled_node_radius * math.sin(angle)
                    adjusted_x1 = x1 + scaled_node_radius * math.cos(angle)
                    adjusted_y1 = y1 + scaled_node_radius * math.sin(angle)

                    arrow_shape = (15, 15, 7) if self.is_directed else None  # Larger arrow
                    self.canvas.create_line(adjusted_x1, adjusted_y1, adjusted_x2, adjusted_y2, fill="gray", width=2 * self.scale, arrow=tk.LAST, arrowshape=arrow_shape)

                    # Draw edge weight
                    idx1 = self._node_to_index[node1_id]
                    idx2 = self._node_to_index[node2_id]
                    weight = self.adj_matrix[idx1][idx2]
                    mid_x = (x1 + x2) / 2
                    mid_y = (y1 + y2) / 2
                    # Adjust font size based on scale, with a minimum size
                    font_size = max(8, int(12 * self.scale))
                    self.canvas.create_text(mid_x, mid_y, text=str(weight), font=("Arial", font_size, "bold"), fill="red")

            # Draw nodes and labels
            for node_id, (x_orig, y_orig) in self.positions.items():
                x, y = _transform_coords(x_orig, y_orig)
                scaled_node_radius = node_radius * self.scale
                self.canvas.create_oval(x - scaled_node_radius, y - scaled_node_radius,
                                        x + scaled_node_radius, y + scaled_node_radius,
                                        fill="skyblue", outline="blue")
                # Adjust font size based on scale, with a minimum size
                font_size = max(8, int(10 * self.scale))
                self.canvas.create_text(x, y, text=str(node_id), font=("Arial", font_size, "bold"))

        def _on_mouse_wheel(event):
            # Respond to Linux (event.num) and Windows/macOS (event.delta)
            if event.num == 4 or event.delta > 0:  # Scroll up (zoom in)
                self.scale *= 1.1
            elif event.num == 5 or event.delta < 0:  # Scroll down (zoom out)
                self.scale /= 1.1
            _draw_elements()

        def _on_mouse_press(event):
            self.last_mouse_x = event.x
            self.last_mouse_y = event.y

        def _on_mouse_drag(event):
            dx = event.x - self.last_mouse_x
            dy = event.y - self.last_mouse_y
            self.offset_x += dx
            self.offset_y += dy
            self.last_mouse_x = event.x
            self.last_mouse_y = event.y
            _draw_elements()

        self.canvas.bind("<ButtonPress-1>", _on_mouse_press)
        self.canvas.bind("<B1-Motion>", _on_mouse_drag)
        self.canvas.bind("<MouseWheel>", _on_mouse_wheel)  # For Windows/macOS
        self.canvas.bind("<Button-4>", _on_mouse_wheel)  # For Linux (scroll up)
        self.canvas.bind("<Button-5>", _on_mouse_wheel)  # For Linux (scroll down)

        _draw_elements()  # Initial draw
        self.window.mainloop()

    


