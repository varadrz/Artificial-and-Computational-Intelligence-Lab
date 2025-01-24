from queue import PriorityQueue  # Import PriorityQueue

def gbfs(graph, start, goal, h):
    open_list, came_from, visited = PriorityQueue(), {start: None}, set()
    open_list.put((h[start], start))  # Store (h(n), node)

    while not open_list.empty():
        _, node = open_list.get()
        if node == goal: return reconstruct(came_from, node)
        visited.add(node)
        for neighbor, _ in graph[node]:
            if neighbor not in visited:
                came_from[neighbor] = node
                open_list.put((h[neighbor], neighbor))
    return None

def reconstruct(came_from, node):
    path = []
    while node:
        path.append(node)
        node = came_from[node]
    return path[::-1]

# Example usage:
graph = {
    'A': [('B', 1), ('F', 2)],
    'B': [('C', 1)],
    'F': [('H', 1)],
    'C': [('D', 1)],
    'H': [('I', 1)],
    'D': [('J', 1)],
    'I': [('J', 1)],
    'J': []
}

# Heuristic (Manhattan distance example) to prioritize the correct nodes
h = {
    'A': 7,  # Starting point
    'B': 6,
    'F': 4,
    'C': 5,
    'H': 3,
    'D': 2,
    'I': 1,
    'J': 0  # Goal point
}

print("GBFS Path:", gbfs(graph, 'A', 'J', h))
