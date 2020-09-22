import math
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def check(m, a, b, c, a_intersect_b, a_intersect_c, b_intersect_c, a_union_b_union_c) -> bool:
            total = 0
            total += m // a + m // b + m // c
            total -= m // a_intersect_b + m // a_intersect_c + m // b_intersect_c
            total += m // a_union_b_union_c 
            return total >= n

        a_intersect_b = a * b // math.gcd(a, b)
        a_intersect_c = a * c // math.gcd(a, c)
        b_intersect_c = b * c // math.gcd(b, c)

        a_union_b_union_c = a * b_intersect_c // math.gcd(a, b_intersect_c)

        l, r = 1, 10 ** 10
        while l < r:
            m = l + (r - l) // 2
            if check(m, a, b, c, a_intersect_b, a_intersect_c, b_intersect_c, a_union_b_union_c):
                r = m
            else:
                l = m + 1
        return l