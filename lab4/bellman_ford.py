from WeightedGraph import WeightedGraph


def read_input():
    f = open("bellman_ford.in", "rt")
    prices_string = f.readline()
    prices = [int(word) for word in prices_string.split() if word.isdigit()]
    discount = int(f.readline())
    f.close()
    return prices, discount


def write_output():
    f = open("bellman_ford.out", "w")
    result = bellman_ford(*read_input())
    f.write(str(result))
    f.close()


def bellman_ford(graph: WeightedGraph, start_elem):
    # parents = {}.fromkeys(graph.vertices)
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

    return sum(paths.values()) / (len(paths) - 1)


if __name__ == '__main__':
    graph2 = WeightedGraph([
        ('s', 't', 6),
        ('s', 'y', 7),
        ('t', 'x', 5),
        ('t', 'y', 8),
        ('t', 'z', -4),
        ('x', 't', -2),
        ('y', 'x', -3),
        ('y', 'z', 9),
        ('z', 's', 2),
        # ('z', 'x', 7)
        ('z', 'x', 4)
    ])
    print(bellman_ford(graph2, 'z'))
