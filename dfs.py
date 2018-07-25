"""Depth First Traversal in a Graph."""

from collections import defaultdict


class Graph:

    def __init__(self):
        """Initialization method that creates a dictionary to store graph."""
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Function that add edge (u, v) to the graph."""
        self.graph[u].append(v)

    def dfs_visit(self, v, visited):
        """Utility function that recursively check for the edges."""
        visited[v] = True
        print(v, end=" ")

        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_visit(i, visited)

    def dfs(self):
        """Function that print the Depth Breadth Traversal from the given source 's'."""
        visited = defaultdict(bool)

        #Traverse all trees in dfs forest
        for i in tuple(self.graph):
            if not visited[i]:
                self.dfs_visit(i, visited)


if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(2, 5)
    g.add_edge(4, 6)
    g.add_edge(5, 10)
    g.add_edge(11, 7)

    print(" " * 10, "Depth First Traversal starting from vertex 0: ")
    g.dfs()
