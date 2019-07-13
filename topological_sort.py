"""Topological Sort in Directed Acyclic Graph(DAG)."""


def dfs_topsort(graph, stack, visited, vertex):
    for v in graph[vertex]:
        if v not in visited:
            visited.append(v)
            dfs_topsort(graph, stack, visited, v)

    stack.insert(0, vertex)


def topological_sort(graph):
    stack = []
    visited = []
    for vertex in graph:
        if vertex not in visited:
            visited.append(vertex)
            dfs_topsort(graph, stack, visited, vertex)

    return stack


if __name__ == "__main__":
    g = {
        0: [],
        1: [],
        2: [3],
        3: [1],
        4: [0, 1],
        5: [0, 2]
    }


    print(topological_sort(g))
