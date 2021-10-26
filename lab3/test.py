import unittest

from lab3.discount import best_purchase


class TestBestPurchase(unittest.TestCase):
    def setUp(self) -> None:
        self.price_1 = [50, 20, 30, 17, 100]
        self.discount_1 = 10

        self.price_2 = [1, 2, 3, 4, 5, 6, 7]
        self.discount_2 = 100

        self.price_3 = [1, 1, 1]
        self.discount_3 = 33

    def test_default_cases(self):
        self.assertEqual(best_purchase(self.price_1, self.discount_1), 207.00)
        self.assertEqual(best_purchase(self.price_2, self.discount_2), 15.00)
        self.assertEqual(best_purchase(self.price_3, self.discount_3), 2.67)

    def test_empty_case(self):
        self.assertEqual(best_purchase([], 10), 0)

    def test_little_case(self):
        self.assertEqual(best_purchase([100, 150], 50), 250)

    def test_equal_case(self):
        self.assertEqual(best_purchase([1, 1, 1, 1], 100), 3)


if __name__ == '__main__':
    unittest.main()
