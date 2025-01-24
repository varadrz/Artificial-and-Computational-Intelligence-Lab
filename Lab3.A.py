#Write a program to implement informed search: a). A* search


from queue import PriorityQueue

def a_star(graph, start, goal, h):
    open_list, g_score, came_from = PriorityQueue(), {start: 0}, {start: None}
    open_list.put((h[start], start))  # Store (f(n), node)
    
    while not open_list.empty():
        _, node = open_list.get()
        if node == goal: return reconstruct(came_from, node)
        for neighbor, cost in graph[node]:
            g = g_score[node] + cost
            if g < g_score.get(neighbor, float('inf')):
                g_score[neighbor], came_from[neighbor] = g, node
                open_list.put((g + h[neighbor], neighbor))
    return None

def reconstruct(came_from, node):
    path = []
    while node:
        path.append(node)
        node = came_from[node]
    return path[::-1]

# Example usage:
graph = {'A': [('B', 1), ('C', 4)], 'B': [('D', 2)], 'C': [('D', 5)], 'D': []}
h = {'A': 7, 'B': 6, 'C': 2, 'D': 0}  # Heuristic (Manhattan distance)
print("A* Path:", a_star(graph, 'A', 'D', h))
