from lab5.Graph import Graph


def tarjan(graph: Graph):
    start_elem = list(graph.vertices)[0]
    ids = dfs(graph, start_elem)
    low_link = []


def dfs(graph: Graph, start_element):
    checking_stack = [].
    visited = []
    on_stack = []
    id_counter = -1
    scc = []
    for vertex in graph.vertices:
        if vertex not in visited:
            checking_stack.append(vertex)
            while checking_stack:
                vertex = checking_stack.pop()

                if vertex not in visited:
                    id_counter += 1
                    on_stack.append(vertex)
                    visited.append(vertex)
                    checking_stack += graph.vertices[vertex]

                elif vertex in on_stack:
                    current_css = [vertex]
                    while (elem := on_stack.pop()) != vertex:
                        current_css.append(elem)
                    scc.append(current_css)

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
    ('y', 'z'),
    ('y', 'l')
    ])
print(dfs(graph2, 's'))
