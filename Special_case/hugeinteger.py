class HugeInteger(list):

    def __init__(self, iterable=[]):
        super().__init__(iterable)

    def __eq__(self, other: HugeInteger):
        if len(self) != len(other):
            return False
        else:
            return all(self[i]==other[i] for i in range(len(self)))

    def __ne__(self, other: HugeInteger):
        return not self.__eq__(other)

    def __gt__(self, other: HugeInteger):
        if len(self) > len(other):
            return True
        if len(self) < len(other):
            return False
        for i in range(len(self) - 1, -1, -1):
            if self[i] > other[i]:
                return True
            if self[i] < other[i]:
                return False
        return False

    def __lt__(self, other):
        if len(self) < len(other):
            return True
        if len(self) > len(other):
            return False
        for i in range(len(self) - 1, -1, -1):
            if self[i] < other[i]:
                return True
            if self[i] > other[i]:
                return False
        return False

    def __ge__(self, other: HugeInteger):
        return self.__gt__(other) or self.__eq__(other)

    def __le__(self, other: HugeInteger):
        return self.__lt__(other) or self.__eq__(other)

    def __add__(self, other):
        sumSize = len(self) + 1 if len(self) >= len(other) else len(other) + 1
        # initialize the sum
        sum = HugeInteger([0 for _ in range(sumSize)])
        if len(self) <= len(other):
            for i in range(len(self)):
                sum[i] = self[i] + other[i]
            for i in range(len(self), len(other)):
                sum[i] = other[i]
        else:
            for i in range(len(other)):
                sum[i] = self[i] + other[i]
            for i in range(len(other), len(self)):
                sum[i] = self[i]
        for i in range(len(sum) - 1):
            if sum[i] > 9:
                sum[i] -= 10
                sum[i + 1] += 1
        if sum[-1] == 0:
            sum.pop()
        return sum

    def __sub__(self, other):
        if len(self) >= len(other):
            diffSize = len(self) + 1
        else:
            diffSize = len(other) + 1
        diff = HugeInteger()
        for i in range(diffSize):
            diff.append(0)

        if len(self) <= len(other):
            for i in range(len(self)):
                diff[i] = self[i] - other[i]
            for i in range(len(self), len(other)):
                diff[i] = other[i]
        else:
            for i in range(len(other)):
                diff[i] = self[i] - other[i]
            for i in range(len(other), len(self)):
                diff[i] = self[i]
        for i in range(len(diff) - 1):
            if diff[i] < 0:
                diff[i] += 10
                diff[i + 1] -= 1
        for i in range(len(diff) - 1, -1, -1):
            if diff[i] != 0:
                break
            else:
                diff.pop(i)

        return diff

    def __mul__(self, other):
        productSize = len(self) + len(other)
        product = HugeInteger()
        for __ in range(productSize):
            product.append(0)

        for i in range(len(self)):
            for x in range(len(other)):
                product[i + x] = product[i + x] + self[i] * other[x]

        for i in range(len(product)):
            if product[i] > 9:
                product[i + 1] += product[i] // 10
                product[i] = product[i] % 10

        for i in range(len(product) - 1, 0, -1):
            if product[i] != 0:
                break
            else:
                product.pop(i)

        return product

    def __floordiv__(self, other):
        #zero = HugeInteger()
        # zero.append(0)
        if self < other:
            return self.zero()
        buffer = HugeInteger()
        quotient = HugeInteger()
        dividend = HugeInteger()

        for i in range(len(self)):
            dividend.append(self[i])

        for __ in range(len(self) - len(other)):
            quotient.append(0)

        for __ in range(len(self)):
            buffer.append(0)

        if buffer <= dividend:
            quotient.append(0)

        if (len(other) == 1) and (other[len(other) - 1] == 0):
            return self.zero()

        for i in range(len(quotient) - 1, -1, -1):
            quotient[i] = 10
            condition = True
            while condition or (other * quotient) > dividend:
                condition = False
                quotient[i] -= 1

        for i in range(len(quotient) - 1, 0, -1):
            if quotient[i] != 0:
                break
            else:
                quotient.pop(i)

        if quotient * other == dividend:
            return quotient

        return quotient

    def __mod__(self, other):
        if self < other:
            return self
        remainder = HugeInteger()
        buffer = HugeInteger()
        buffer = other * (self // other)
        remainder = self - buffer
        return remainder

    def __pow__(self, other):
        binary = HugeInteger()
        convertBinary(other, binary)
        binary.reverse()
        power = self.one()
        base = self
        for i in range(len(binary)):
            if binary[i] == 1:
                power = power * base
            base = base * base

        return power

    def __rshift__(self, other):
        power = self.two() ** other
        #assert self//power > self.one()
        return self // power

    def __lshift__(self, other):
        power = self.two() ** other
        #assert self//power > self.one()
        return self * power

    def zero(self):
        zero = HugeInteger()
        zero.append(0)

        return zero

    def one(self):
        one = HugeInteger()
        one.append(1)

        return one

    def two(self):
        two = HugeInteger()
        two.append(2)

        return two


def convertBinary(num, binary):
    if num // num.two() != num.zero():
        convertBinary(num // num.two(), binary)
    assert len(num % num.two()) == 1
    temp = (num % num.two())[0]
    binary.append(temp)


def modular_pow(base, exponent, modulo):
    if modulo == base.one():
        return base.zero()
    result = base.one()
    base = base % modulo
    while exponent > base.zero():
        if exponent % base.two() == base.one():
            result = result * base % modulo
        exponent = exponent >> base.one()
        base = base * base % modulo

    return result


def printHugeinteger(num):
    num.reverse()
    for i in num:
        print(i, end="")


def inputHugeinteger(string):
    assert string.isdigit()
    string = string[::-1]
    integer = HugeInteger()
    for i in string:
        integer.append(int(i))

    return integer


import random

small_primes = [2,
                3,    5,    7,    11,   13,   17,   19,   23,   29,   31,
                37,   41,   43,   47,   53,   59,   61,   67,   71,   73,
                79,   83,   89,   97,   101,  103,  107,  109,  113,  127,
                131,  137,  139,  149,  151,  157,  163,  167,  173,  179,
                181,  191,  193,  197,  199,  211,  223,  227,  229,  233,
                239,  241,  251,  257,  263,  269,  271,  277,  281,  283,
                293,  307,  311,  313,  317,  331,  337,  347,  349,  353,
                359,  367,  373,  379,  383,  389,  397,  401,  409,  419,
                421,  431,  433,  439,  443,  449,  457,  461,  463,  467,
                479,  487,  491,  499,  503,  509,  521,  523,  541,  547,
                557,  563,  569,  571,  577,  587,  593,  599,  601,  607,
                613,  617,  619,  631,  641,  643,  647,  653,  659,  661,
                673,  677,  683,  691,  701,  709,  719,  727,  733,  739,
                743,  751,  757,  761,  769,  773,  787,  797,  809,  811,
                821,  823,  827,  829,  839,  853,  857,  859,  863,  877,
                881,  883,  887,  907,  911,  919,  929,  937,  941,  947,
                953,  967,  971,  977,  983,  991,  997,  1009, 1013, 1019,
                1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087,
                1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151, 1153,
                1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229,
                1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291, 1297,
                1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381,
                1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451, 1453,
                1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523,
                1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583, 1597,
                1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663,
                1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741,
                1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811, 1823,
                1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901,
                1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987, 1993,
                1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063,
                2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129, 2131,
                2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221,
                2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287, 2293,
                2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371,
                2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437,
                2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531, 2539,
                2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621,
                2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687, 2689,
                2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749,
                2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819, 2833,
                2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909,
                2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999, 3001,
                3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083,
                3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187,
                3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257, 3259,
                3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343,
                3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413, 3433,
                3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517,
                3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571, 3581,
                3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659,
                3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727, 3733,
                3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823,
                3833, 3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911,
                3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967, 3989, 4001
                ]


import random


def miller_rabin(m):
    k = 5
    s = 1
    t = HugeInteger()
    t = (m - m.one()) // m.two()

    if len(m) == 1:
        if m[0] == 2 or m[0] == 3:
            return True

    for p in small_primes:
        primeNum = HugeInteger()

        while p > 0:
            primeNum.append(p % 10)
            p //= 10

        if primeNum * primeNum <= m:

            if m % primeNum == m.zero() and m // primeNum > m.one():
                return False

            if m % primeNum == m.zero() and m // primeNum == m.one():
                return True

    while t % m.two() == m.zero():
        t = t // m.two()
        s += 1

    for r in range(0, k):
        temp = HugeInteger()
        temp = m - m.one()
        temp.reverse()
        tempstr = ''
        for i in temp:
            tempstr += str(i)
        tempstr = int(tempstr)
        rand_num = random.randint(1, tempstr)
        rand = HugeInteger()
        while rand_num > 0:
            rand.append(rand_num % 10)
            rand_num //= 10
        y = modular_pow(rand, t, m)
        prime = False

        if (y == m.one()):
            prime = True

        for i in range(0, s):
            if (y == m - m.one()):
                prime = True
                break
            else:
                y = (y * y) % m

        if not prime:
            return False

    return True
