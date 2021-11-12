from WeightedGraph import WeightedGraph


def read_input():
    f = open("bellman_ford.in", "rt")
    num_edges, start_elem = f.readline().split()
    input_lists = []
    for line in f:
        vertex, child, weight = line.split()
        input_lists.append([vertex, child, int(weight)])
    f.close()
    return start_elem, input_lists


def write_output():
    f = open("bellman_ford.out", "w")
    start_elem, input_lists = read_input()
    graph = WeightedGraph(input_lists)
    result = bellman_ford(graph, start_elem)
    f.write(str(result))
    f.close()


def bellman_ford(graph: WeightedGraph, start_elem):
    paths = {}.fromkeys(graph.vertices, float("inf"))
    paths[start_elem] = 0
    for _ in range(len(graph.vertices) - 1):
        for vertex in graph.vertices:
            for child in graph.vertices[vertex]:
                paths[child] = min(paths[child], paths[vertex] + graph.vertices[vertex][child])
    for vertex in graph.vertices:
        for child in graph.vertices[vertex]:
            if paths[child] > paths[vertex] + graph.vertices[vertex][child]:
                return False
    res_paths = [value for value in paths.values() if value != float("inf")]
    return sum(res_paths) / (len(res_paths) - 1)


if __name__ == '__main__':
    write_output()
