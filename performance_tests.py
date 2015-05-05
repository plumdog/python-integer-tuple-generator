from __future__ import print_function
import time
import collections
import itertools

import integer_tuple_generator


Result = collections.namedtuple('Result', ['name', 'time', 'exception'])


class PerformanceTestCase(object):

    def tearDown(self):
        self.end = time.time()
        print('{id}: {timetaken}'.format(
            id=self.id, timetaken=self.end - self.start))

    def run_method(self, method_name):
        func = getattr(self, method_name)
        try:
            start = time.time()
            result = func()
            end = time.time()
            timetaken = end - start
        except NotImplementedError:
            timetaken = None
            result = None

        try:
            self.verify_result(method_name, result)
        except ValueError as ex:
            pass
        else:
            ex = None
        return Result('{klass}.{func}'.format(klass=self.__class__.__name__, func=method_name),
                      time=timetaken, exception=ex)

    def verify_result(self, method_name, result):
        pass

    def run_tests(self):
        results = []
        for attr in dir(self):
            if attr.startswith('test_'):
                results.append(self.run_method(attr))
        results = sorted(results, key=lambda r: r.name)
        name_width = max(len(result.name) for result in results)
        time_width = max(len(str(result.time)) for result in results)

        any_exceptions = any(result.exception for result in results)

        if any_exceptions:
            exception_width = max(len(str(result.exception)) for result in results)
        else:
            exception_width = 0

        total_width = name_width + time_width + 3
        if any_exceptions:
            total_width += exception_width + 3
        heading = '{name} | {time}'.format(name='Test Name'.ljust(name_width),
                                           time='Time'.ljust(time_width))
        if any_exceptions:
            heading += ' | {exception}'.format(exception='Exception'.ljust(exception_width))
        print(heading)
        print('-'*total_width)
        for result in results:
            line = '{test_name} | {time}'.format(test_name=result.name.ljust(name_width),
                                                 time=str(result.time).ljust(time_width))
            if any_exceptions:
                if result.exception:
                    line += ' | {exception}'.format(exception=str(result.exception))
                else:
                    line += ' |'
            print(line)
        print()


class IntsPerformanceTestCaseBase(PerformanceTestCase):

    LENGTHS = {
        'test_2_dimensions_upto_2000': 2003001,
        'test_3_dimensions_upto_200': 1373701,
        'test_4_dimensions_upto_70': 1150626,
        'test_5_dimensions_upto_40': 1221759,
        'test_6_dimensions_upto_25': 736281,
        'test_7_dimensions_upto_20': 888030,
        'test_8_dimensions_upto_15': 490314,
        'test_9_dimensions_upto_13': 497420}

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

    def verify_result(self, method_name, result):
        if result is None:
            return
        length = self.LENGTHS.get(method_name)
        result_length = len(result)
        if length is not None:
            if result_length != length:
                raise ValueError('{result_length} != {length}'.format(
                    result_length=result_length, length=length))
        else:
            raise ValueError('Nothing to compare')


class IntsPerformanceTestCase(IntsPerformanceTestCaseBase):
    def test_2_dimensions_upto_2000(self):
        return list(integer_tuple_generator.ints(2, 2000))

    def test_3_dimensions_upto_200(self):
        return list(integer_tuple_generator.ints(3, 200))

    def test_4_dimensions_upto_70(self):
        return list(integer_tuple_generator.ints(4, 70))

    def test_5_dimensions_upto_40(self):
        return list(integer_tuple_generator.ints(5, 40))

    def test_6_dimensions_upto_25(self):
        return list(integer_tuple_generator.ints(6, 25))

    def test_7_dimensions_upto_20(self):
        return list(integer_tuple_generator.ints(7, 20))

    def test_8_dimensions_upto_15(self):
        return list(integer_tuple_generator.ints(8, 15))

    def test_9_dimensions_upto_13(self):
        return list(integer_tuple_generator.ints(9, 13))


class IntsPerformanceTestCaseNaive(IntsPerformanceTestCaseBase):
    def test_2_dimensions_upto_2000(self):
        l = []
        for x in range(0, 2001):
            for y in range(0, 2001):
                if x + y > 2000:
                    break
                l.append((x, y))
        return l

    def test_3_dimensions_upto_200(self):
        l = []
        for x in range(0, 201):
            for y in range(0, 201):
                for z in range(0, 201):
                    if x + y + z > 200:
                        break
                    l.append((x, y, z))
        return l


    def test_4_dimensions_upto_70(self):
        l = []
        for w in range(0, 71):
            for x in range(0, 71):
                for y in range(0, 71):
                    for z in range(0, 71):
                        if w + x + y + z > 70:
                            break
                        l.append((w, x, y, z))
        return l

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
        return l

    def test_6_dimensions_upto_25(self):
        l = []
        for u in range(0, 26):
            for v in range(0, 26):
                for w in range(0, 26):
                    for x in range(0, 26):
                        for y in range(0, 26):
                            for z in range(0, 26):
                                if u + v + w + x + y + z > 25:
                                    break
                                l.append((u, v, w, x, y, z))
        return l


class IntsPerformanceTestCaseSmarter(IntsPerformanceTestCaseBase):
    def test_2_dimensions_upto_2000(self):
        l = []
        for x in range(0, 2001):
            for y in range(0, 2001):
                if x + y > 2000:
                    break
                l.append((x, y))
        return l

    def test_3_dimensions_upto_200(self):
        l = []
        for x in range(0, 201):
            for y in range(0, 201):
                xy = x + y
                if xy > 200:
                    break
                for z in range(0, 201):
                    if xy + z > 200:
                        break
                    l.append((x, y, z))
        return l

    def test_4_dimensions_upto_70(self):
        l = []
        for w in range(0, 71):
            for x in range(0, 71):
                wx = w + x
                if wx > 70:
                    break
                for y in range(0, 71):
                    wxy = wx + y
                    if wxy > 70:
                        break
                    for z in range(0, 71):
                        if wxy + z > 70:
                            break
                        l.append((w, x, y, z))
        return l

    def test_5_dimensions_upto_40(self):
        l = []
        for v in range(0, 41):
            for w in range(0, 41):
                vw = v + w
                if vw > 40:
                    break
                for x in range(0, 41):
                    vwx = vw + x
                    if vwx > 40:
                        break
                    for y in range(0, 41):
                        vwxy = vwx + y
                        if vwxy > 40:
                            break
                        for z in range(0, 41):
                            if vwxy + z > 40:
                                break
                            l.append((v, w, x, y, z))
        return l

    def test_6_dimensions_upto_25(self):
        l = []
        for u in range(0, 26):
            for v in range(0, 26):
                uv = u + v
                if uv > 25:
                    break
                for w in range(0, 26):
                    uvw = uv + w
                    if uvw > 25:
                        break
                    for x in range(0, 26):
                        uvwx = uvw + x
                        if uvwx > 25:
                            break
                        for y in range(0, 26):
                            uvwxy = uvwx + y
                            if uvwxy > 25:
                                break
                            for z in range(0, 26):
                                if uvwxy + z > 25:
                                    break
                                l.append((u, v, w, x, y, z))
        return l

    def test_7_dimensions_upto_20(self):
        l = []
        for t in range(0, 21):
            for u in range(0, 21):
                tu = t + u
                if tu > 20:
                    break
                for v in range(0, 21):
                    tuv = tu + v
                    if tuv > 20:
                        break
                    for w in range(0, 21):
                        tuvw = tuv + w
                        if tuvw > 20:
                            break
                        for x in range(0, 21):
                            tuvwx = tuvw + x
                            if tuvwx > 20:
                                break
                            for y in range(0, 21):
                                tuvwxy = tuvwx + y
                                if tuvwxy > 20:
                                    break
                                for z in range(0, 21):
                                    if tuvwxy + z > 20:
                                        break
                                    l.append((t, u, v, w, x, y, z))
        return l

    def test_8_dimensions_upto_15(self):
        l = []
        for s in range(0, 16):
            for t in range(0, 16):
                st = s + t
                if st > 15:
                    break
                for u in range(0, 16):
                    stu = st + u
                    if stu > 15:
                        break
                    for v in range(0, 16):
                        stuv = stu + v
                        if stuv > 15:
                            break
                        for w in range(0, 16):
                            stuvw = stuv + w
                            if stuvw > 15:
                                break
                            for x in range(0, 16):
                                stuvwx = stuvw + x
                                if stuvwx > 15:
                                    break
                                for y in range(0, 16):
                                    stuvwxy = stuvwx + y
                                    if stuvwxy > 15:
                                        break
                                    for z in range(0, 16):
                                        if stuvwxy + z > 15:
                                            break
                                        l.append((s, t, u, v, w, x, y, z))
        return l

    def test_9_dimensions_upto_13(self):
        l = []
        for r in range(0, 14):
            for s in range(0, 14):
                rs = r + s
                if rs > 13:
                    break
                for t in range(0, 14):
                    rst = rs + t
                    if rst > 13:
                        break
                    for u in range(0, 14):
                        rstu = rst + u
                        if rstu > 13:
                            break
                        for v in range(0, 14):
                            rstuv = rstu + v
                            if rstuv > 13:
                                break
                            for w in range(0, 14):
                                rstuvw = rstuv + w
                                if rstuvw > 13:
                                    break
                                for x in range(0, 14):
                                    rstuvwx = rstuvw + x
                                    if rstuvwx > 13:
                                        break
                                    for y in range(0, 14):
                                        rstuvwxy = rstuvwx + y
                                        if rstuvwxy > 13:
                                            break
                                        for z in range(0, 14):
                                            if rstuvwxy + z > 13:
                                                break
                                            l.append((r, s, t, u, v, w, x, y, z))
        return l


class IntsPerformanceTestCaseItertools(IntsPerformanceTestCaseBase):
    def test_2_dimensions_upto_2000(self):
        l = []
        for x, y in itertools.product(range(0, 2001), range(0, 2001)):
            if x + y > 2000:
                continue
            l.append((x, y))
        return l

    def test_3_dimensions_upto_200(self):
        l = []
        for x, y, z in itertools.product(range(0, 201), range(0, 201), range(0, 201)):
            if x + y + z > 200:
                continue
            l.append((x, y, z))
        return l

    def test_4_dimensions_upto_70(self):
        l = []
        for w, x, y, z in itertools.product(range(0, 71), range(0, 71), range(0, 71), range(0, 71)):
            if w + x + y + z > 70:
                continue
            l.append((w, x, y, z))
        return l


if __name__ == '__main__':
    IntsPerformanceTestCase().run_tests()
    IntsPerformanceTestCaseNaive().run_tests()
    IntsPerformanceTestCaseSmarter().run_tests()
    IntsPerformanceTestCaseItertools().run_tests()
