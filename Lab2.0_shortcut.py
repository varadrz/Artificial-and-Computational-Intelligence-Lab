from collections import deque

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
    'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': ['G', 'H'], 'D': ['I'], 'I': ['M'], 
    'E': ['J', 'K'], 'K': ['N'], 'G': ['L'], 'F': [], 'N': [], 'L': [], 'H': [], 'J': [], 'M': []
}

start, goal = 'A', 'M'
path = bfs(graph, start, goal)

print(f"The shortest path from {start} to {goal} is: {path}" if path else f"No path found from {start} to {goal}.")
