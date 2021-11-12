import unittest

from lab4.WeightedGraph import WeightedGraph
from lab4.bellman_ford import bellman_ford


class TestBestPurchase(unittest.TestCase):
    def setUp(self) -> None:
        self.dijkstra_1_graph = WeightedGraph([
            (0, 3, 8),
            (1, 4, 9),
            (4, 2, 4),
            (5, 0, 9),
            (5, 4, 6),
            (5, 1, 7),
            (1, 2, 1),
            (3, 1, 0)
        ])

        self.cormen_1_graph = WeightedGraph([
            ('s', 't', 6),
            ('s', 'y', 7),
            ('t', 'x', 5),
            ('t', 'y', 8),
            ('t', 'z', -4),
            ('x', 't', -2),
            ('y', 'x', -3),
            ('y', 'z', 9),
            ('z', 's', 2),
            ('z', 'x', 7)
        ])

        self.cormen_2_graph = WeightedGraph([
            ('s', 't', 6),
            ('s', 'y', 7),
            ('t', 'x', 5),
            ('t', 'y', 8),
            ('t', 'z', -4),
            ('x', 't', -2),
            ('y', 'x', -3),
            ('y', 'z', 9),
            ('z', 's', 2),
            ('z', 'x', 4)
        ])

        self.simple_positive_cycle_graph = WeightedGraph([
            ('a', 'b', 2),
            ('b', 'a', 10),
            ('b', 'c', 4),
            ('c', 'a', 100)
        ])

        self.little_graph = WeightedGraph([
            ('a', 'b', 2)
        ])
    def test_non_negative_case(self):
        self.assertEqual(bellman_ford(self.dijkstra_1_graph, 5), 9.4)

    def test_normal_case(self):
        self.assertEqual(bellman_ford(self.cormen_1_graph, 'z'), 5.25)

    def test_negative_cycle(self):
        self.assertEqual(bellman_ford(self.cormen_2_graph, 'z'), False)

    def test_positive_cycle(self):
        self.assertEqual(bellman_ford(self.simple_positive_cycle_graph, 'a'), 4)

    def test_little_case(self):
        self.assertEqual(bellman_ford(self.little_graph, 'a'), 2)


if __name__ == '__main__':
    unittest.main()
