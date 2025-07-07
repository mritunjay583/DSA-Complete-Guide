import tkinter as tk
import math
from typing import Optional, Dict, Tuple
from pytree.node import Node

class Visualizer:
    """
    A utility class to generate a string representation of a tree.
    """
    @staticmethod
    def get_tree_string(root: Optional[Node]) -> str:
        """
        Generates a graphical string representation of the tree.

        Args:
            root: The root node of the tree to visualize.

        Returns:
            A string containing the formatted tree.
        """
        if not root:
            return "(Empty Tree)"
        
        lines = []
        Visualizer._generate_lines(root, "", True, lines)
        return "\n".join(lines)

    @staticmethod
    def _generate_lines(node: Node, prefix: str, is_last: bool, lines: list[str]):
        """
        Recursively generates the lines for the tree representation.

        Args:
            node: The current node to process.
            prefix: The prefix string for the current line (indentation and connectors).
            is_last: True if the node is the last child of its parent.
            lines: The list to append the generated lines to.
        """
        if node is not None:
            lines.append(f"{prefix}{'└── ' if is_last else '├── '}{node.value}")
            children = [node.left, node.right]
            children = [child for child in children if child is not None]
            
            new_prefix = prefix + ("    " if is_last else "│   ")
            
            for i, child in enumerate(children):
                is_last_child = (i == len(children) - 1)
                Visualizer._generate_lines(child, new_prefix, is_last_child, lines)

class GUIVisualizer:
    """
    A class to create a GUI visualization of a tree using tkinter.
    """
    def __init__(self, root: Optional[Node]):
        self.root = root
        self.window = tk.Tk()
        self.window.title("Tree Visualization")
        self.canvas = tk.Canvas(self.window, width=800, height=600, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.scale = 1.0
        self.offset_x = 0
        self.offset_y = 0
        self.last_mouse_x = 0
        self.last_mouse_y = 0
        self.dragged_node_value: Optional[any] = None # Store the value of the node being dragged

        self.node_radius = 20
        self.v_spacing = 80  # Vertical spacing between levels
        self.h_spacing = 60  # Horizontal spacing between sibling subtrees

        self.node_positions: Dict[any, Tuple[float, float]] = {} # Stores (x,y) for each node
        self.node_map: Dict[any, Node] = {} # Maps node value to Node object for quick lookup
        self.x_coords_at_level: Dict[int, float] = {} # To keep track of the next available x-coordinate for each level

        if self.root:
            self._populate_node_map(self.root)
            self._calculate_tree_positions(self.root, 0) # Initial layout calculation
            self._normalize_positions()

    def show(self):
        """
        Displays the tkinter window with the tree visualization.
        This method starts the tkinter event loop.
        """
        self.canvas.bind("<ButtonPress-1>", self._on_mouse_press)
        self.canvas.bind("<B1-Motion>", self._on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self._on_mouse_release)
        self.canvas.bind("<MouseWheel>", self._on_mouse_wheel)  # For Windows/macOS
        self.canvas.bind("<Button-4>", self._on_mouse_wheel)  # For Linux (scroll up)
        self.canvas.bind("<Button-5>", self._on_mouse_wheel)  # For Linux (scroll down)

        self._draw_elements()  # Initial draw
        self.window.mainloop()

    def _populate_node_map(self, node: Node):
        if node:
            self.node_map[node.value] = node
            self._populate_node_map(node.left)
            self._populate_node_map(node.right)

    def _calculate_tree_positions(self, node: Node, level: int):
        if not node:
            return

        # Recursively calculate positions for children first (post-order traversal)
        self._calculate_tree_positions(node.left, level + 1)
        self._calculate_tree_positions(node.right, level + 1)

        # Assign y-coordinate based on level
        y = level * self.v_spacing

        # Calculate x-coordinate for current node
        x = 0
        if node.left and node.right:
            # Center between children
            x = (self.node_positions[node.left.value][0] + self.node_positions[node.right.value][0]) / 2
        elif node.left:
            # Position relative to left child
            x = self.node_positions[node.left.value][0] + self.h_spacing
        elif node.right:
            # Position relative to right child
            x = self.node_positions[node.right.value][0] - self.h_spacing
        else: # Leaf node
            # Assign a unique x-position for leaf nodes at this level
            if level not in self.x_coords_at_level:
                self.x_coords_at_level[level] = 0
            x = self.x_coords_at_level[level]
            self.x_coords_at_level[level] += self.h_spacing * 2 # Ensure enough space for leaves

        # Ensure no overlap with previously placed nodes at the same level
        if level in self.x_coords_at_level and x < self.x_coords_at_level[level]:
            x = self.x_coords_at_level[level]
            self.x_coords_at_level[level] += self.h_spacing * 2

        self.node_positions[node.value] = (x, y)

    def _normalize_positions(self):
        # Find min/max x and y to calculate overall tree dimensions
        min_x = min(pos[0] for pos in self.node_positions.values())
        max_x = max(pos[0] for pos in self.node_positions.values())
        min_y = min(pos[1] for pos in self.node_positions.values())
        max_y = max(pos[1] for pos in self.node_positions.values())

        tree_width = max_x - min_x
        tree_height = max_y - min_y

        # Calculate offsets to center the tree on the canvas
        center_x_offset = (self.canvas.winfo_width() - tree_width) / 2 - min_x
        center_y_offset = (self.canvas.winfo_height() - tree_height) / 2 - min_y

        # Apply centering offsets to all node positions
        for node_value in self.node_positions:
            x, y = self.node_positions[node_value]
            self.node_positions[node_value] = (x + center_x_offset, y + center_y_offset)

    def _transform_coords(self, x_orig, y_orig):
        return (x_orig * self.scale + self.offset_x, y_orig * self.scale + self.offset_y)

    def _draw_elements(self):
        self.canvas.delete("all")  # Clear canvas

        scaled_node_radius = self.node_radius * self.scale
        
        # Draw edges first
        for node_value, (x_orig, y_orig) in self.node_positions.items():
            node = self.node_map.get(node_value)
            if node:
                x, y = self._transform_coords(x_orig, y_orig)

                if node.left:
                    left_x_orig, left_y_orig = self.node_positions[node.left.value]
                    left_x, left_y = self._transform_coords(left_x_orig, left_y_orig)
                    self._draw_line_with_arrow(x, y, left_x, left_y, scaled_node_radius)

                if node.right:
                    right_x_orig, right_y_orig = self.node_positions[node.right.value]
                    right_x, right_y = self._transform_coords(right_x_orig, right_y_orig)
                    self._draw_line_with_arrow(x, y, right_x, right_y, scaled_node_radius)

        # Draw nodes and labels
        for node_value, (x_orig, y_orig) in self.node_positions.items():
            x, y = self._transform_coords(x_orig, y_orig)
            self.canvas.create_oval(x - scaled_node_radius, y - scaled_node_radius,
                                    x + scaled_node_radius, y + scaled_node_radius,
                                    fill="lightblue", outline="black", tags=f"node_{node_value}")
            font_size = max(8, int(10 * self.scale))
            self.canvas.create_text(x, y, text=str(node_value), font=("Arial", font_size, "bold"), tags=f"node_{node_value}_text")

    def _draw_line_with_arrow(self, x1, y1, x2, y2, scaled_node_radius):
        # Calculate adjusted endpoints for arrow to be outside the node
        angle = math.atan2(y2 - y1, x2 - x1)
        adjusted_x2 = x2 - scaled_node_radius * math.cos(angle)
        adjusted_y2 = y2 - scaled_node_radius * math.sin(angle)
        adjusted_x1 = x1 + scaled_node_radius * math.cos(angle)
        adjusted_y1 = y1 + scaled_node_radius * math.sin(angle)

        arrow_shape = (15, 15, 7)  # Larger arrow for clarity
        self.canvas.create_line(adjusted_x1, adjusted_y1, adjusted_x2, adjusted_y2,
                                fill="gray", width=2 * self.scale, arrow=tk.LAST, arrowshape=arrow_shape)

    def _find_node_at_coords(self, event_x, event_y):
        # Iterate through nodes and check if event coordinates are within any node
        for node_value, (x_orig, y_orig) in self.node_positions.items():
            x, y = self._transform_coords(x_orig, y_orig)
            scaled_node_radius = self.node_radius * self.scale
            distance = math.sqrt((event_x - x)**2 + (event_y - y)**2)
            if distance <= scaled_node_radius:
                return node_value
        return None

    def _on_mouse_wheel(self, event):
        # Get mouse position on canvas
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)

        # Calculate current world coordinates under mouse
        world_x = (x - self.offset_x) / self.scale
        world_y = (y - self.offset_y) / self.scale

        if event.num == 4 or event.delta > 0:  # Scroll up (zoom in)
            self.scale *= 1.1
        elif event.num == 5 or event.delta < 0:  # Scroll down (zoom out)
            self.scale /= 1.1
        
        # Adjust offset to keep the world point under the mouse fixed
        self.offset_x = x - world_x * self.scale
        self.offset_y = y - world_y * self.scale

        self._draw_elements()

    def _on_mouse_press(self, event):
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y
        self.dragged_node_value = self._find_node_at_coords(event.x, event.y)
        if self.dragged_node_value:
            self.canvas.itemconfig(f"node_{self.dragged_node_value}", fill="red") # Highlight dragged node

    def _on_mouse_drag(self, event):
        dx = event.x - self.last_mouse_x
        dy = event.y - self.last_mouse_y
        
        if self.dragged_node_value:
            # Update the original position of the dragged node
            current_x, current_y = self.node_positions[self.dragged_node_value]
            self.node_positions[self.dragged_node_value] = (current_x + dx / self.scale, current_y + dy / self.scale)
        else:
            # Pan the canvas
            self.offset_x += dx
            self.offset_y += dy
        
        self.last_mouse_x = event.x
        self.last_mouse_y = event.y
        self._draw_elements()

    def _on_mouse_release(self, event):
        if self.dragged_node_value:
            self.canvas.itemconfig(f"node_{self.dragged_node_value}", fill="lightblue") # Unhighlight node
            self.dragged_node_value = None