from __future__ import print_function
import time
import collections
import itertools

import integer_tuple_generator


Result = collections.namedtuple('Result', ['name', 'time'])


class PerformanceTestCase(object):
    def tearDown(self):
        self.end = time.time()
        print('{id}: {timetaken}'.format(
            id=self.id, timetaken=self.end - self.start))

    def run_method(self, method_name):
        func = getattr(self, method_name)
        try:
            start = time.time()
            func()
            end = time.time()
            timetaken = end - start
        except NotImplementedError:
            timetaken = None
        return Result('{klass}.{func}'.format(klass=self.__class__.__name__, func=method_name),
                      timetaken)

    def run_tests(self):
        results = []
        for attr in dir(self):
            if attr.startswith('test_'):
                results.append(self.run_method(attr))
        results = sorted(results, key=lambda r: r.name)
        width = max(len(result.name) for result in results)
        time_width = 20
        print('Test'.ljust(width), '|', 'Time')
        print('-'*(width + time_width + 3))
        for result in results:
            print(result.name.ljust(width), '|', result.time)
        print()


class IntsPerformanceTestCaseBase(PerformanceTestCase):
    def test_2_dimensions_upto_2000(self):
        raise NotImplementedError

    def test_3_dimensions_upto_200(self):
        raise NotImplementedError

    def test_4_dimensions_upto_70(self):
        raise NotImplementedError

    def test_5_dimensions_upto_40(self):
        raise NotImplementedError

    def test_6_dimensions_upto_25(self):
        raise NotImplementedError

    def test_7_dimensions_upto_20(self):
        raise NotImplementedError

    def test_8_dimensions_upto_15(self):
        raise NotImplementedError

    def test_9_dimensions_upto_13(self):
        raise NotImplementedError


class IntsPerformanceTestCase(IntsPerformanceTestCaseBase):
    def test_2_dimensions_upto_2000(self):
        list(integer_tuple_generator.ints(2, 2000))

    def test_3_dimensions_upto_200(self):
        list(integer_tuple_generator.ints(3, 200))

    def test_4_dimensions_upto_70(self):
        list(integer_tuple_generator.ints(4, 70))

    def test_5_dimensions_upto_40(self):
        list(integer_tuple_generator.ints(5, 40))

    def test_6_dimensions_upto_25(self):
        list(integer_tuple_generator.ints(6, 25))

    def test_7_dimensions_upto_20(self):
        list(integer_tuple_generator.ints(7, 20))

    def test_8_dimensions_upto_15(self):
        list(integer_tuple_generator.ints(8, 15))

    def test_9_dimensions_upto_13(self):
        list(integer_tuple_generator.ints(9, 13))


class IntsPerformanceTestCaseNaive(IntsPerformanceTestCaseBase):
    def test_2_dimensions_upto_2000(self):
        l = []
        for x in range(0, 2001):
            for y in range(0, 2001):
                if x + y > 2000:
                    break
                l.append((x, y))

    def test_3_dimensions_upto_200(self):
        l = []
        for x in range(0, 201):
            for y in range(0, 201):
                for z in range(0, 201):
                    if x + y + z > 200:
                        break
                    l.append((x, y, z))


    def test_4_dimensions_upto_70(self):
        l = []
        for w in range(0, 71):
            for x in range(0, 71):
                for y in range(0, 71):
                    for z in range(0, 71):
                        if w + x + y + z > 70:
                            break
                        l.append((w, x, y, z))

    def test_5_dimensions_upto_40(self):
        l = []
        for v in range(0, 41):
            for w in range(0, 41):
                for x in range(0, 41):
                    for y in range(0, 41):
                        for z in range(0, 41):
                            if v + w + x + y + z > 40:
                                break
                            l.append((v, w, x, y, z))

    def test_6_dimensions_upto_25(self):
        l = []
        for u in range(0, 26):
            for v in range(0, 26):
                for w in range(0, 26):
                    for x in range(0, 26):
                        for y in range(0, 26):
                            for z in range(0, 26):
                                if u + v + w + x + y + z > 40:
                                    break
                                l.append((u, v, w, x, y, z))


class IntsPerformanceTestCaseItertools(IntsPerformanceTestCaseBase):
    def test_2_dimensions_upto_2000(self):
        l = []
        for x, y in itertools.product(range(0, 2001), range(0, 2001)):
            if x + y > 2000:
                continue
            l.append((x, y))

    def test_3_dimensions_upto_200(self):
        l = []
        for x, y, z in itertools.product(range(0, 201), range(0, 201), range(0, 201)):
            if x + y + z > 200:
                continue
            l.append((x, y, z))

    def test_4_dimensions_upto_70(self):
        l = []
        for w, x, y, z in itertools.product(range(0, 71), range(0, 71), range(0, 71), range(0, 71)):
            if w + x + y + z > 70:
                continue
            l.append((w, x, y, z))

    # def test_5_dimensions_upto_40(self):
    #     l = []
    #     for v, w, x, y, z in itertools.product(range(0, 41), range(0, 41), range(0, 41), range(0, 41), range(0, 41)):
    #         if v + w + x + y + z > 40:
    #             continue
    #         l.append((v, w, x, y, z))
        
                
if __name__ == '__main__':
    IntsPerformanceTestCase().run_tests()
    IntsPerformanceTestCaseNaive().run_tests()
    IntsPerformanceTestCaseItertools().run_tests()
