class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min = float("inf")
        max = 0
        s = set()
        for i in nums:
            if i>=0:
                s.add(i)
                if i<min:
                    min = i
                if i>max:
                    max = i
        if min>1:
            return 1

        for i in range(min, max+1):
            if i not in s:
                return i
        return max+1