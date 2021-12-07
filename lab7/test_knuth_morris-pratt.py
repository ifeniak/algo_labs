import unittest
from knuth_morris_pratt import search


class TestKnuthMorrisPratt(unittest.TestCase):

    def test_knuth_morris_pratt_1(self):
        self.assertEqual(search("QWERTY", ""), 0)

    def test_knuth_morris_pratt_2(self):
        self.assertEqual(search("QWERTY", "WE"), 1)

    def test_knuth_morris_pratt_3(self):
        self.assertEqual(search("QWERTY", "QWEEE"), -1)

    def test_knuth_morris_pratt_4(self):
        self.assertEqual(search("Hello, world!", "o, wo"), 4)

    def test_knuth_morris_pratt_5(self):
        self.assertEqual(search("vhdsbvbsdbvdsjkksd", "bsdbv"), 6)

    def test_knuth_morris_pratt_6(self):
        self.assertEqual(search("vhdsbvbsdbvdsjkksd", "bsdbvv"), -1)