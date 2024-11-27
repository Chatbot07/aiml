def aStarAlgo(start_node, stop_node):
    open_set = set([start_node])  # Use set([]) to initialize
    closed_set = set()
    g = {}  # Store distance from starting node
    parents = {}  # Store parent relationships

    g[start_node] = 0  # Distance from start to itself is 0
    parents[start_node] = start_node  # Root node points to itself

    while len(open_set) > 0:
        # Find the node with the lowest f(n) = g(n) + h(n)
        n = None
        for v in open_set:
            if n is None or g[v] + heuristic(v) < g[n] + heuristic(n):
                n = v

        if n == stop_node:
            # Reconstruct path from start_node to stop_node
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            path.append(start_node)
            path.reverse()
            print(f"Path found: {path}")
            return path

        for (m, weight) in get_neighbors(n):
            if m not in open_set and m not in closed_set:
                open_set.add(m)
                parents[m] = n
                g[m] = g[n] + weight
            else:
                if g[m] > g[n] + weight:
                    g[m] = g[n] + weight
                    parents[m] = n
                    if m in closed_set:
                        closed_set.remove(m)
                        open_set.add(m)

        open_set.remove(n)
        closed_set.add(n)

    print("Path does not exist!")
    return None

def get_neighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    return None

def heuristic(n):
    # Heuristic values (Manhattan or straight-line distance to goal)
    H_dist = {
        'A': 6,
        'B': 4,
        'C': 2,
        'D': 1,
        'E': 0
    }
    return H_dist[n]

# Graph definition
Graph_nodes = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3)],
    'C': [('D', 1), ('E', 5)],
    'D': [('E', 2)],
}

# Perform A* Search from 'A' to 'E'
aStarAlgo('A', 'E')
