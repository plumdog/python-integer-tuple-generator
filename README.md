# python-integer-tuple-generator
Efficiently generate tuples of integers.

If you want to iterate over all possible tuples of integers that sum
upto a given value, you've come to the right place.

Install with `pip install integer-tuple-generator`

Then iterate as follows:

```python
import integer_tuple_generator

# To iterate over all 3-tuples that have sum less-than or equal to 100
for a, b, c in integer_tuple_generator.ints(3, upto_sum=100):
    print(a, b, c)
```

The integers are also guaranteed to be generated in sorted order.

At present, this is slightly slower than nested for-loops, if you
include the necessary temporary sums and checks (see
`performance_tests.py`) but this makes it easy to loop over a
dynamic-number of integers.

TODO
----
See if there are ways to make it faster. Either in Python or Cython.
