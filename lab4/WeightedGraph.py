

class WeightedGraph:
    def __init__(self, input_lists: [[]]):
        self.vertices = {first_elem: {} for first_elem, second_elem, third_elem in input_lists}
        for vertex, child, weight in input_lists:
            self.vertices[vertex][child] = weight
            if child not in self.vertices.keys():
                self.vertices[child] = {}
