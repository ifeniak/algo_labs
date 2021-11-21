import unittest
from main import find_ways


class FindWaysCountTest(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix1 = [
            ["a", "a", "a"],
            ["c", "a", "b"],
            ["d", "e", "f"]
        ]
        self.matrix2 = [['a', 'b', 'c', 'd', 'e', 'f', 'a', 'g', 'h', 'i']]
        self.matrix3 = [
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"],
            ["a", "a", "a", "a", "a", "a", "a"]
        ]

    def test_first_case(self):
        self.assertEqual(find_ways(self.matrix1, 3, 3), 5)

    def test_second_case(self):
        self.assertEqual(find_ways(self.matrix2, 10, 1), 2)

    def test_third_class(self):
        self.assertEqual(find_ways(self.matrix3, 7, 6), 201684)
