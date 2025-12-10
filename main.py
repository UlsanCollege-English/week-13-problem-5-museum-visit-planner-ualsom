from collections import deque

def shortest_path(rooms, doors, start, goal):
    """
    Compute one shortest path between start and goal in an undirected graph.

    rooms: list of room name strings.
    doors: list of (a, b) pairs, each pair is an undirected door between rooms a and b.
    start: start room name.
    goal: goal room name.

    Return:
      - list of room names from start to goal (inclusive) for one shortest path,
      - [start] if start == goal,
      - [] if no path exists.
    """

    # If start or goal doesn't exist, no path possible
    if start not in rooms or goal not in rooms:
        return []

    # Start equals goal
    if start == goal:
        return [start]

    # Build adjacency list
    adj = {r: set() for r in rooms}
    for a, b in doors:
        if a in adj and b in adj:
            adj[a].add(b)
            adj[b].add(a)

    # BFS setup
    queue = deque([start])
    visited = {start}
    parent = {start: None}

    # BFS loop
    while queue:
        node = queue.popleft()

        if node == goal:
            break  # Stop BFS early when goal is reached

        for neigh in adj[node]:
            if neigh not in visited:
                visited.add(neigh)
                parent[neigh] = node
                queue.append(neigh)

    # If goal was never visited, no path
    if goal not in parent:
        return []

    # Reconstruct path from goal → start
    path = []
    cur = goal
    while cur is not None:
        path.append(cur)
        cur = parent[cur]

    path.reverse()
    return path


if __name__ == "__main__":
    rooms = ["Entrance", "Hall", "Gallery", "Cafe"]
    doors = [("Entrance", "Hall"), ("Hall", "Gallery"), ("Gallery", "Cafe")]
    print(shortest_path(rooms, doors, "Entrance", "Cafe"))
