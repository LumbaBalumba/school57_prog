import unittest
import random
from quicksort import quicksort


class SortTester(unittest.TestCase):
    def simple_test(self):
        ARR_SIZE = 10
        arr = [random.randint(-100, 100) for _ in range(ARR_SIZE)]
        self.assertEqual(quicksort(arr), sorted(arr))

    def test_sortedness(self):
        ARR_SIZE = 10**4
        arr = [random.randint(-100, 100) for _ in range(ARR_SIZE)]
        self.assertEqual(quicksort(arr), sorted(arr))
