import itertools


def sums_to(total, dimensions):
    """Generates all lists that sum to `total` with length
    `dimensions`.

    """
    for i in range(0, total + 1):
        if dimensions == 2:
            yield [i, total - i]
        else:
            for subsum in sums_to(i, dimensions - 1):
                subsum.append(total - i)
                yield subsum


def ints(dimensions=2, upto_sum=None):
    """Generate tuples of size `dimensions`. If upto_sum is given, then
    the generator is finite and stops once all tuples that sum to
    less-than-or-equal-to `upto_sum`.

    """
    for i in itertools.count():
        if upto_sum and (i > upto_sum):
            break
        else:
            for sum_ in sums_to(i, dimensions):
                yield tuple(sum_)
