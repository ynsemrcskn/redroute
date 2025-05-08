import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os
import sys

from topology import create_topology
from strategy import find_shortest_path

def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class NetworkGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Simulation: Shortest Path Finder")
        self.root.iconbitmap(resource_path("icon.ico"))
        self.root.geometry("900x700")
        self.root.configure(bg="#fff5f5")

        self.graph, self.hosts, self.pos = create_topology()

        self.build_interface()
        self.draw_network()

    def build_interface(self):
        style = ttk.Style()
        style.theme_use("clam")  # Better for custom theming

        # Red background styles
        style.configure("Red.TFrame", background="#fff5f5")
        style.configure("Red.TLabelframe", background="#fff5f5", foreground="#b22222", font=("Helvetica", 10, "bold"))
        style.configure("Red.TLabelframe.Label", background="#fff5f5", foreground="#b22222")

        # Label and Combobox styling
        style.configure("TLabel", background="#fff5f5", font=("Helvetica", 10))
        style.configure("TCombobox", fieldbackground="#ffeaea", background="#fff5f5")

        # Button styling
        style.configure("TButton", background="#ffdddd", foreground="#a00", font=("Helvetica", 10, "bold"))

        # === Header ===
        header_frame = ttk.Frame(self.root, style="Red.TFrame")
        header_frame.pack(pady=10)
        title = ttk.Label(header_frame, text="📡 Conceptual Network Simulation", font=("Helvetica", 20, "bold"), foreground="#b22222")
        subtitle = ttk.Label(header_frame, text="Visualizing the shortest path between selected hosts", font=("Helvetica", 12), foreground="#555")
        title.pack()
        subtitle.pack()

        # === Controls ===
        control_frame = ttk.LabelFrame(self.root, text="Select Hosts", padding=10, style="Red.TLabelframe")
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="Select Source Host:", font=("Helvetica", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.source_var = tk.StringVar()
        self.source_menu = ttk.Combobox(control_frame, textvariable=self.source_var, values=self.hosts, state="readonly", width=20)
        self.source_menu.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(control_frame, text="Select Destination Host:", font=("Helvetica", 10)).grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.dest_var = tk.StringVar()
        self.dest_menu = ttk.Combobox(control_frame, textvariable=self.dest_var, values=self.hosts, state="readonly", width=20)
        self.dest_menu.grid(row=1, column=1, padx=5, pady=5)

        ttk.Button(control_frame, text="🔍 Find Shortest Path", command=self.display_shortest_path).grid(row=2, column=0, columnspan=2, pady=10)

        # === Matplotlib Graph ===
        self.figure = plt.Figure(figsize=(7, 5))
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(pady=10)

        # === Status Bar ===
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor="w", font=("Helvetica", 9), bg="#f5dddd", fg="#a00")
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=3)

    def draw_network(self, path=None):
        self.ax.clear()
        node_colors = []
        for n in self.graph.nodes:
            if self.graph.nodes[n]['type'] == 'host':
                node_colors.append('#ff9999')  # Light red for hosts
            else:
                node_colors.append('#ffcccb')  # Pinkish for switches

        nx.draw(
            self.graph, self.pos, ax=self.ax,
            with_labels=True, node_color=node_colors,
            node_size=600, edge_color='gray', font_size=8, font_weight='bold'
        )

        if path:
            edges = list(zip(path, path[1:]))
            nx.draw_networkx_edges(self.graph, self.pos, edgelist=edges, ax=self.ax, edge_color='red', width=2)

        self.canvas.draw()

    def display_shortest_path(self):
        src = self.source_var.get()
        dst = self.dest_var.get()
        if not src or not dst:
            messagebox.showwarning("Selection Error", "Please select both a source and destination host.")
            self.status_var.set("Selection Error: Missing source or destination.")
            return
        if src == dst:
            messagebox.showwarning("Selection Error", "Source and destination cannot be the same.")
            self.status_var.set("Selection Error: Source and destination are the same.")
            return

        self.status_var.set(f"Finding shortest path from {src} to {dst}...")
        path = find_shortest_path(self.graph, src, dst)
        if path:
            self.draw_network(path)
            path_str = " ➜ ".join(path)
            self.status_var.set(f"✅ Shortest path found: {path_str}")
        else:
            self.draw_network()
            self.status_var.set("❌ No path exists between the selected nodes.")
            messagebox.showinfo("No Path", "No path exists between the selected nodes.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkGUI(root)
    root.mainloop()
