from lab5.Graph import Graph


def tarjan(graph: Graph):
    start_elem = list(graph.vertices)[0]
    ids = dfs(graph, start_elem)
    low_link = []


def dfs(graph: Graph, start_element):
    checking_stack = []
    visited = []
    on_stack = []
    ids = {}
    low_links = []
    id_counter = -1
    for vertex in graph.vertices:
        if vertex not in visited:
            checking_stack.append(vertex)
            while checking_stack:
                vertex = checking_stack.pop()

                if vertex not in visited:
                    id_counter += 1
                    ids[vertex] = id_counter

                    low_links.append(id_counter)
                    on_stack.append(id_counter)
                    visited.append(vertex)
                    checking_stack += graph.vertices[vertex]

                elif ids[vertex] in on_stack:
                    lowest_link = min(low_links[ids[vertex]], low_links[id_counter])
                    for i in range(len(on_stack) - 1, ids[vertex] - 1, -1):
                        low_links[on_stack[i]] = lowest_link
                        on_stack.pop()

    return ids, low_links


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
