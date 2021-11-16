from lab5.Graph import Graph


def tarjan(graph: Graph):
    checking_stack = []
    visited = []
    on_stack = []
    scc = []
    for vertex in graph.vertices:
        if vertex not in visited:
            checking_stack.append(vertex)
            while checking_stack:
                vertex = checking_stack.pop()

                if vertex not in visited:
                    on_stack.append(vertex)
                    visited.append(vertex)
                    checking_stack += graph.vertices[vertex]

                elif vertex in on_stack:
                    current_scc = [vertex]
                    while (elem := on_stack.pop()) != vertex:
                        current_scc.append(elem)
                    scc.append(current_scc)
    return scc


graph2 = Graph([
    ('s', 't'),
    ('u', 't'),
    ('u', 'v'),
    ('s', 'w'),
    ('w', 's'),
    ('t', 'x'),
    ('x', 'u'),
    ('u', 'y'),
    ('v', 'y'),
    ('z', 'v'),
    ('w', 'x'),
    ('x', 'y'),
    ('y', 'z')
    ])
print(tarjan(graph2))
