from copy import deepcopy
from typing import List


def dfs(graph: List[List[float]], source: int, sink: int, parent: List[int]) -> bool:
    """
    Depth-first search (DFS) to find a path from source to sink in the residual graph.

    Args:
    - graph (List[List[float]]): The residual graph represented as an adjacency matrix.
    - source (int): The index of the source node.
    - sink (int): The index of the sink node.
    - parent (List[int]): An array to store the parent node of each vertex in the augmenting path.

    Returns:
    - bool: True if there exists an augmenting path from source to sink, False otherwise.
    """
    # Initializes visited array to track visited nodes
    visited = [False] * len(graph)
    stack = []
    stack.append(source)
    visited[source] = True

    # Performs DFS
    while stack:
        u = stack.pop()
        for ind, val in enumerate(graph[u]):
            # Check if the node is not visited and there is a residual capacity
            if not visited[ind] and val > 0:
                stack.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[sink] else False


def compute_max_flow(graph: List[List[float]], source: int, sink: int) -> float:
    """
    Computes the maximum flow in a graph using Depth-First Search. We look for augmenting paths that increase the flow from source to sink.

    Args:
    - graph (List[List[float]]): The flow network represented as an adjacency matrix.
    - source (int): The index of the source node.
    - sink (int): The index of the sink node.

    Returns:
    - float: The maximum flow from source to sink in the given graph.
    """
    # Creates a copy of the original graph to store residual capacities
    residual_graph = deepcopy(graph)
    parent = [-1] * len(
        graph
    )  # Array to store the parent of each node in the augmenting path for traversal
    max_flow = 0

    # While there exists an augmenting path from source to sink
    while dfs(residual_graph, source, sink, parent):
        path_flow = float("Inf")  # Initialize path flow to infinity
        s = sink

        # Find the minimum residual capacity of the augmenting path
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink

        # Update residual capacities of the edges and reverse edges along the augmenting path
        while v != source:
            u = parent[v]
            # We subtract the flow from the forward edge and add it to the reverse edge to allow for the situation where the optimal path is not the shortest path
            residual_graph[u][v] -= path_flow
            residual_graph[v][
                u
            ] += path_flow  # Remove this line to get the shortest path
            v = parent[v]

    return max_flow


# Test cases
def test_case_1():
    graph = [
        [0.0, 16.0, 13.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 10.0, 12.0, 0.0, 0.0],
        [0.0, 4.0, 0.0, 0.0, 14.0, 0.0],
        [0.0, 0.0, 9.0, 0.0, 0.0, 20.0],
        [0.0, 0.0, 0.0, 7.0, 0.0, 4.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ]

    assert compute_max_flow(graph, 0, 5) == 23


def test_case_2():
    graph = [
        [0.0, 10.0, 10.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 2.0, 4.0, 8.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 9.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 10.0],
        [0.0, 0.0, 0.0, 6.0, 0.0, 10.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ]

    assert compute_max_flow(graph, 0, 5) == 19


def test_case_3():
    graph = [
        [0.0, 9.0, 0.0, 4.0, 0.0, 0.0],
        [0.0, 0.0, 8.0, 0.0, 0.0, 0.0],
        [0.0, 0.0, 0.0, 5.0, 0.0, 3.0],
        [0.0, 0.0, 0.0, 0.0, 7.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 8.0],
        [0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
    ]

    assert compute_max_flow(graph, 0, 5) == 10


def test_case_4():
    graph = [
        [0.0, 10.0, 10.0, 0.0],
        [0.0, 0.0, 5.0, 10.0],
        [0.0, 0.0, 0.0, 10.0],
        [0.0, 0.0, 0.0, 0.0],
    ]

    assert compute_max_flow(graph, 0, 3) == 20


if __name__ == "__main__":
    test_case_1()
    test_case_2()
    test_case_3()
    test_case_4()
    print("All test cases passed")
