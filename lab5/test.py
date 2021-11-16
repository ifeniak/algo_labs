import unittest

from lab5.Graph import Graph
from lab5.tarjan import tarjan


class TestBestPurchase(unittest.TestCase):
    def setUp(self) -> None:
        self.tarjan_1_graph = Graph([
            (0, 3),
            (1, 4),
            (4, 2),
            (5, 0),
            (5, 4),
            (5, 1),
            (1, 2),
            (3, 1)
        ])

        self.cormen_1_graph = Graph([
            ('s', 't'),
            ('s', 'y'),
            ('t', 'x'),
            ('t', 'y'),
            ('t', 'z'),
            ('x', 't'),
            ('y', 'x'),
            ('y', 'z'),
            ('z', 's'),
            ('z', 'x')
        ])

        self.cormen_2_graph = Graph([
            ('s', 't'),
            ('s', 'y'),
            ('t', 'x'),
            ('t', 'y'),
            ('t', 'z'),
            ('x', 't'),
            ('y', 'x'),
            ('y', 'z'),
            ('z', 's'),
            ('z', 'x')
        ])

        self.simple_positive_cycle_graph = Graph([
            ('a', 'b'),
            ('b', 'a'),
            ('b', 'c'),
            ('c', 'a')
        ])

        self.little_graph = Graph([
            ('a', 'b', 2)
        ])
    def test_non_negative_case(self):
        self.assertEqual(tarjan(self.tarjan_1_graph), [[1, 2], [5, 3]])

    def test_normal_case(self):
        self.assertEqual(tarjan(self.tarjan_1_graph), [['q', 'f', 's'], ['r']])

    def test_negative_cycle(self):
        self.assertEqual(tarjan(self.cormen_2_graph), False)

    def test_positive_cycle(self):
        self.assertEqual(tarjan(self.simple_positive_cycle_graph), 4)

    def test_little_case(self):
        self.assertEqual(tarjan(self.little_graph), [['4', '6', 'ss', 'a'], ['3', 'd', 'f'], ['e']])


if __name__ == '__main__':
    unittest.main()