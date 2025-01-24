from collections import deque

def breadth_first_search (graph, start, goal):
    """Perform Breadth-First Search to find the shortest path from start to goal."""

    #Initialize the queue with the start node and an empty path
    queue = deque([[start]])
    visited = set()

    while queue:
        #Dequeue the first path from the queue
        path = queue.popleft()
        node = path[-1]                 #get the last node in the path

        #Check if the node has already been visited
        if node in visited:
            continue

        #Mark the node as visited
        visited.add (node)

        #Check if the goal has been reached
        if node == goal:
            return path
        
        #Add all unvisited neighbours to the queue
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                new_path = list (path)
                new_path.append(neighbor)
                queue.append(new_path)

    #Return none if no path is found
    return None

#Define the graph as an adjacency list

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

# Test the breadth_first_search function
start_node = 'A'
goal_node = 'M'
path = breadth_first_search(graph, start_node, goal_node)

if path:
    print(f"The shortest path from {start_node} to {goal_node} is: {path}")
else:
    print(f"No path found from {start_node} to {goal_node}.")