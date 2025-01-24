from collections import deque
import networkx as nx
import matplotlib.pyplot as plt

def bfs(graph, start, goal):
    queue, visited = deque([[start]]), set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node in visited: continue
        if node == goal: return path
        visited.add(node)
        queue.extend(path + [n] for n in graph.get(node, []) if n not in visited)
    return None


graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I'],
    'I': ['M'],
    'E': ['J', 'K'],
    'K': ['N'],
    'G': ['L'],
    'F': [],
    'N': [],
    'L': [],
    'H': [],
    'J': [],
    'M': []
}


start, goal = 'A', 'M'
path = bfs(graph, start, goal)

print(f"The shortest path from {start} to {goal} is: {path}" if path else f"No path found from {start} to {goal}.")

# Plotting the graph using NetworkX
G = nx.Graph()

# Add edges to the graph
for node, neighbors in graph.items():
    for neighbor in neighbors:
        G.add_edge(node, neighbor)

# Define positions for the nodes using a layout
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=3000, font_size=10, font_weight='bold', edge_color='gray')

# Highlight the path found, if exists
if path:
    edges_in_path = [(path[i], path[i+1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges_in_path, edge_color='r', width=3)

plt.show()
