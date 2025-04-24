import matplotlib.pyplot as plt
import networkx as nx
from collections import deque

class NetworkTraversal:
    def __init__(self):
        self.graph = {}
        # Mapping of nodes to IP addresses
        self.ip_addresses = {
            'A': "192.168.1.1",
            'B': "192.168.1.2",
            'C': "192.168.1.3",
            'D': "192.168.1.4",
            'E': "192.168.1.5",
            'F': "192.168.1.6",
            'G': "192.168.1.7"
        }

    def add_edge(self, u, v):
        self.graph.setdefault(u, []).append(v)

    def dfs_traversal(self, start, goal):
        visited = set()
        visit_order = []
        used_edges = []
        found = [False]

        print("\n🟢 DFS Traversal from", start, "to", goal + ":")

        def dfs(node):
            if found[0]:
                return
            visited.add(node)
            visit_order.append(node)
            print(f"Visit: {node} (IP: {self.ip_addresses[node]})")  # Displaying IP address
            if node == goal:
                found[0] = True
                return
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited and not found[0]:
                    used_edges.append((node, neighbor))
                    dfs(neighbor)
            if not found[0]:
                print(f"Backtrack from: {node} (IP: {self.ip_addresses[node]})")  # Displaying IP address

        dfs(start)
        return visit_order, used_edges

    def draw_graph(self, dfs_nodes, dfs_edges):
        G = nx.DiGraph()
        for node in self.graph:
            for neighbor in self.graph[node]:
                G.add_edge(node, neighbor)

        # Update this layout if you change graphs
        pos = {
            'A': (2, 3),
            'B': (1, 2),
            'C': (3, 2),
            'D': (0.5, 1),
            'E': (1.5, 1),
            'F': (2.5, 1),
            'G': (3.5, 1)
        }

        fig, ax = plt.subplots(figsize=(8, 7))
        nx.draw(G, pos, with_labels=False, node_color='skyblue', node_size=2000,
                font_size=16, arrows=True, ax=ax, arrowstyle='-|>', arrowsize=20)

        # Custom node labels with numbering and IP addresses
        labels = {}
        for idx, node in enumerate(dfs_nodes):
            labels[node] = f"{node} ({self.ip_addresses[node]})"

        # Fallback to original label if not visited
        for node in G.nodes:
            if node not in labels:
                labels[node] = node

        nx.draw_networkx_labels(G, pos, labels, font_size=14, ax=ax)
        nx.draw_networkx_edges(G, pos, edgelist=dfs_edges, edge_color='orange', width=3, ax=ax, arrows=True)
        ax.set_title(f'DFS Traversal from {dfs_nodes[0]} to {dfs_nodes[-1]}', fontsize=16)
        ax.axis('off')

        plt.tight_layout()
        plt.show()

# === Main Execution ===
if __name__ == "__main__":
    print("=== 🌐 Packet Routing Simulation ===")
    nt = NetworkTraversal()

    # Example: Tree-like Hierarchy
    nt.add_edge('A', 'B')
    nt.add_edge('A', 'C')
    nt.add_edge('B', 'D')
    nt.add_edge('B', 'E')
    nt.add_edge('C', 'F')
    nt.add_edge('C', 'G')

    # Ask user for start and end nodes for DFS
    source = input("Enter the start node for DFS: ")
    destination = input("Enter the destination node for DFS: ")

    print("Source Node:", source)
    print("Destination Node:", destination)

    # Run DFS with user input
    dfs_order, dfs_edges = nt.dfs_traversal(source, destination)

    print("\n✅ Final DFS Visit Order:", ' -> '.join(dfs_order))

    # Draw Graph for DFS
    nt.draw_graph(dfs_order, dfs_edges)


#OUTPUT
# start_letter = 'A'
# target_letter = 'G'

# "Source Node: A
# Destination Node: G

# 🟢 DFS Traversal from A to G:
# Visit: A (IP: 192.168.1.1)
# Visit: B (IP: 192.168.1.2)
# Visit: D (IP: 192.168.1.4)
# Backtrack from: D (IP: 192.168.1.4)
# Visit: E (IP: 192.168.1.5)
# Backtrack from: E (IP: 192.168.1.5)
# Backtrack from: B (IP: 192.168.1.2)
# Visit: C (IP: 192.168.1.3)
# Visit: F (IP: 192.168.1.6)
# Backtrack from: F (IP: 192.168.1.6)
# Visit: G (IP: 192.168.1.7)

# ✅ Final DFS Visit Order: A -> B -> D -> E -> C -> F -> G


#ALgo

# Core Concept
# DFS explores a graph by moving as deep as possible down one path before backtracking.

# Key Characteristics
# Data Structure: Stack (LIFO)
# Approach: "Go deep first"
# Memory: O(depth) - efficient for deep graphs
# Completeness: Yes (for finite graphs)
# Optimality: No (doesn't guarantee shortest path)

# Basic Algorithm
# Start at root node
# Explore deepest unvisited node first
# Backtrack when no more unvisited neighbors

# When to Use
# ✔ Maze solving
# ✔ Topological sorting
# ✔ Cycle detection
# ✔ Puzzle games (e.g., Sudoku)
# ✖ Finding shortest paths

# Time Complexity
# Worst Case: O(V + E)
# (V = vertices, E = edges)

# Comparison

# Feature	      |  BFS	                 |    DFS
# Data Structure  |	Queue	                 |   Stack
# Path Finding	  |  Shortest (unweighted)   |	Not guaranteed
# Memory	      |  O(b^d)	                 |     O(d)
# Best For	      |  Wide, shallow graphs    |	Deep graphs