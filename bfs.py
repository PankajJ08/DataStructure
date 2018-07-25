"""Breadth First Traversal in a Graph."""

from collections import defaultdict, deque


class Graph:

    def __init__(self):
        """Initialization method that creates a dictionary to store graphs."""
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Function that add edge (u, v) to the graph."""
        self.graph[u].append(v)

    def bfs(self, s):
        """Function that print the Breadth First Traversal from the given source 's'."""
        visited = defaultdict(bool)
        dist = defaultdict(int)
        queue = deque()
        queue.append(s)
        visited[s] = True
        dist[s] = 0

        while queue:
            d = queue.popleft()
            print(d, end=" ")

            for i in self.graph[d]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
                    dist[i] = dist[d] + 1


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 10)
    g.add_edge(5, 7)
    print(" " * 10, "Breadth First Traversal starting from vertex 1: ")
    g.bfs(0)
