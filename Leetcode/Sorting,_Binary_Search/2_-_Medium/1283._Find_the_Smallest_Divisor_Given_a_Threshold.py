class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(d):
            s = 0
            for i in nums:
                s += i // d
                if i % d != 0:
                    s+=1
            return s <= threshold
        l, r = 1, max(nums)
        while l < r:
            m = l + (r-l)//2
            if check(m):
                r = m
            else:
                l = m + 1
        return l