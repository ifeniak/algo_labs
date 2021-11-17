import unittest

from lab5.Graph import Graph
from lab5.tarjan import tarjan_new


class TestBestPurchase(unittest.TestCase):
    def setUp(self) -> None:
        self.simple_graph = Graph([
            (0, 1),
            (1, 0),
            (0, 2),
            (4, 2),
            (5, 4),
            (3, 5),
            (2, 3),
            (3, 1),
            (3, 6)
        ])

        self.cormen_1_graph = Graph([
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
        ])

        self.cormen_2_graph = Graph([
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

        self.simple_graph_with_isolated_elements = Graph([
            (0, 1),
            (1, 0),
            (0, 2),
            (4, 2),
            (5, 4),
            (3, 5),
            (2, 3),
            (3, 1),
            (3, 6),
            (100, 1000)
        ])

    def test_simple_case(self):
        self.assertEqual(tarjan_new(self.simple_graph), [[6], [0, 4, 5, 3, 2, 1]])

    def test_only_sccs_case(self):
        self.assertEqual(tarjan_new(self.cormen_1_graph), [['v', 'z', 'y'], ['t', 'u', 'x'], ['s', 'w']])

    def test_sccs_with_free_element(self):
        self.assertEqual(tarjan_new(self.cormen_2_graph), [['l'], ['v', 'z', 'y'], ['t', 'u', 'x'], ['s', 'w']])

    def test_forest_case(self):
        self.assertEqual(tarjan_new(self.simple_graph_with_isolated_elements), [[6], [0, 4, 5, 3, 2, 1], [1000], [100]])


if __name__ == '__main__':
    unittest.main()
