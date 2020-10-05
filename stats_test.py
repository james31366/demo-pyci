from unittest import TestCase

from stats import stdev
from stats import variance


class StatsTest(TestCase):

    def test_variance_typical_values(self):
        """variance of some typical values"""
        self.assertEqual(0.0, variance([10.0, 10.0, 10.0, 10.0, 10.0]))
        self.assertEqual(2.0, variance([1, 2, 3, 4, 5]))
        self.assertEqual(8.0, variance([10, 2, 8, 4, 6]))

    def test_variance_single_value_is_zero(self):
        """variance of a singleton list should be zero"""
        self.assertEqual(0.0, variance([0.0]))
        self.assertEqual(0.0, variance([99.999]))

    def test_variance_throws_exception(self):
        """variance of an empty list should raise an exception"""
        with self.assertRaises(ValueError):
            var = variance([])

    def test_stdev(self):
        """Standard Deviation is sqrt of variance"""
        self.assertEqual(0.0, stdev([2, 2, 2, 2]))
        self.assertEqual(0.5, stdev([1, 1, 2, 2]))


if __name__ == '__main__':
    import unittest

    unittest.main(verbosity=1)
