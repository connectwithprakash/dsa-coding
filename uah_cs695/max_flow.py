from copy import deepcopy


def dfs(graph, source, sink, parent):
    visited = [False] * len(graph)
    stack = []
    stack.append(source)
    visited[source] = True

    while stack:
        u = stack.pop()
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                stack.append(ind)
                visited[ind] = True
                parent[ind] = u

    return True if visited[sink] else False


def compute_max_flow(graph, source, sink):
    residual_graph = deepcopy(graph)
    parent = [-1] * len(graph)
    max_flow = 0

    while dfs(residual_graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, residual_graph[parent[s]][s])
            s = parent[s]

        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            residual_graph[u][v] -= path_flow
            residual_graph[v][u] += path_flow
            v = parent[v]

    return max_flow


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
