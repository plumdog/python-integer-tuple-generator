import unittest
import operator
import functools

from integer_tuple_generator import ints


def ncr(n, r):
    r = min(r, n-r)
    if r == 0:
        return 1
    return (functools.reduce(operator.mul, range(n, n-r, -1), 1)
            // functools.reduce(operator.mul, range(1, r + 1), 1))


def figurate_number(r, n):
    """Returns the nth r-figurate number."""
    return ncr(n + r - 1, r)


class IntegerTupleTestCase(unittest.TestCase):
    def assert_tuple_list_equal(self, a, b):
        self.assertEqual(sorted(a), sorted(b))
        self.assert_correct_order(a)
        self.assert_correct_order(b)

    def assert_correct_order(self, a):
        self.assertEqual(sorted(a, key=lambda b: sum(b)), a)

    def test_two_d_upto_three(self):
        self.assert_tuple_list_equal(
            list(ints(2, 3)),
            [(0, 0), (0, 1), (1, 0), (0, 2), (1, 1), (2, 0), (0, 3), (1, 2), (2, 1), (3, 0)])

    def test_three_d_upto_three(self):
        self.assert_tuple_list_equal(
            list(ints(3, 3)),
            [(0, 0, 0),
             (0, 0, 1), (0, 1, 0), (1, 0, 0),
             (0, 0, 2), (0, 1, 1), (1, 0, 1), (0, 2, 0), (1, 1, 0), (2, 0, 0),
             (0, 0, 3), (0, 1, 2), (1, 0, 2), (0, 2, 1), (1, 1, 1),
             (2, 0, 1), (0, 3, 0), (1, 2, 0), (2, 1, 0), (3, 0, 0)])

    def test_four_d_upto_two(self):
        self.assert_tuple_list_equal(
            list(ints(4, 2)),
            [(0, 0, 0, 0), (0, 0, 0, 1), (0, 0, 1, 0), (0, 1, 0, 0), (1, 0, 0, 0),
             (0, 0, 0, 2), (0, 0, 1, 1), (0, 1, 0, 1), (1, 0, 0, 1), (0, 0, 2, 0),
             (0, 1, 1, 0), (1, 0, 1, 0), (0, 2, 0, 0), (1, 1, 0, 0), (2, 0, 0, 0)])

    def test_lengths(self):
        for n in range(2, 10):
            for upto in range(2, 10):
                self.assertEqual(len(list(ints(n, upto))),
                                 figurate_number(n, upto+1))


if __name__ == '__main__':
    unittest.main()
