from lab5.Graph import Graph


def tarjan_new(graph: Graph):
    visited = []
    on_stack = []
    ids = {}
    low_links = {}
    scc = []
    id_counter = 0

    def dfs(source, id_counter):
        if source not in visited:
            ids[source] = id_counter
            low_links[source] = id_counter
            id_counter += 1
            visited.append(source)
            on_stack.append(source)

            for child in graph.vertices[source]:
                if child not in visited:
                    dfs(child, id_counter)
                    low_links[source] = min(low_links[child], low_links[source])
                elif child in on_stack:
                    low_links[source] = min(low_links[child], low_links[source])

            if low_links[source] == ids[source]:
                current_scc = [source]
                while (elem := on_stack.pop()) != source:
                    current_scc.append(elem)
                scc.append(current_scc)

    for vertex in graph.vertices:
        dfs(vertex, id_counter)
    return scc
