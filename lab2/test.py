import unittest

from lab2.HashTable import HashTable


class TestHashTable(unittest.TestCase):
    def setUp(self) -> None:
        self.hash_table = HashTable(8, [2, 's', 7, 1, 15, '`'])
        self.hash_table_array = [['s', '`'], [2], [7, 15], [], [1], [], [], []]

    def test_insert(self):
        self.hash_table.insert(4)
        self.hash_table_array = [['s', '`'], [2], [7, 15], [4], [1], [], [], []]
        self.assertEqual(self.hash_table._array, self.hash_table_array)

    def test_search(self):
        self.assertEqual(0, self.hash_table.search('s'))
        self.assertEqual(None, self.hash_table.search(0))

    def test_get(self):
        self.assertEqual(1, self.hash_table.get(1))
        self.assertEqual(None, self.hash_table.get(0))

    def test_delete(self):
        self.hash_table.delete('s')
        self.hash_table_array = [['`'], [2], [7, 15], [], [1], [], [], []]
        self.assertEqual(self.hash_table_array, self.hash_table._array)


if __name__ == '__main__':
    unittest.main()
