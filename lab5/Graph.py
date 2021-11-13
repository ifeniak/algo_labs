from lab5.Vertex import Vertex


class Graph:
    def __init__(self, input_tuples: [()]):
        self.vertices = {first_elem: [] for first_elem, second_elem in input_tuples}
        for vertex, child in input_tuples:
            self.vertices[vertex].append(child)
            if child not in self.vertices.keys():
                self.vertices[child] = []
