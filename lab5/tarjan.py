from lab5.Graph import Graph


def tarjan(graph: Graph):
    start_elem = list(graph.vertices)[0]
    ids = dfs(graph, start_elem)
    low_link = []


def dfs(graph: Graph, start_element):
    checking_stack = []
    visited = []
    on_stack = [False] * len(graph.vertices)
    ids = {}
    low_links = []
    id_counter = 0
    for vertex in graph.vertices:
        if vertex not in visited:
            checking_stack.append(vertex)
            while checking_stack:
                vertex = checking_stack.pop()
                if vertex not in visited:
                    ids[vertex] = id_counter
                    low_links.append(id_counter)
                    on_stack[id_counter] = True
                    id_counter += 1
                    visited.append(vertex)
                    checking_stack += graph.vertices[vertex]
                elif on_stack[ids[vertex]]:
                    prev_id = id_counter - 1
                    lowest_link = min(low_links[ids[vertex]], low_links[prev_id])
                    if lowest_link == low_links[ids[vertex]]:
                        for i in range(ids[vertex], len(on_stack)):
                            if on_stack[i]:
                                low_links[i] = lowest_link
                                on_stack[i] = False

    return ids, low_links


graph2 = Graph([
    ('s', 't'),
    ('u', 't',),
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
