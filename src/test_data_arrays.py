import unittest
import random
import numpy as np
from src.data_arrays import DataArrays
from collections import Counter


class TestDataArrays(unittest.TestCase):
    data_arrays: DataArrays

    def setUp(self):
        self.data_arrays = DataArrays()

    def test_remove_duplicates(self):
        a = np.random.randint(0, 9, 200)
        final_array = self.data_arrays.remove_duplicates(a)
        s = Counter(final_array)
        for key in s.keys():
            self.assertEqual(s[key], 1)

    def test_sort_with_duplicates(self):
        a = np.random.randint(0, 9, 200)
        sorted_a = self.data_arrays.sort(a)
        self.assertLess(len(sorted_a), len(a))

    def test_sort_with_decimals(self):
        a = np.random.rand(200)
        sorted_a = self.data_arrays.sort(a)
        i = 0
        while i < (len(sorted_a)-1):
            self.assertLess(sorted_a[i], sorted_a[i+1])
            i += 1
