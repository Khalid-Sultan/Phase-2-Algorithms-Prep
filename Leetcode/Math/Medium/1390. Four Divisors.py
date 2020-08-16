class Solution:
    def find_factors(self, n):
        factors = []
        i = 1
        j = n
        while True:
            if i*j == n:
                factors.append(i)
                if i == j:
                    break
                factors.append(j)
                if len(factors)>4:
                    break
            i += 1
            j = n // i
            if i > j:
                break
        if len(factors)!=4:
            return [0,0,0,0]
        return factors
    def sumFourDivisors(self, nums: List[int]) -> int:
        d = 0
        for i in nums:
            f = self.find_factors(i)
            d+=f[0]+f[1]+f[2]+f[3]
        return d
            