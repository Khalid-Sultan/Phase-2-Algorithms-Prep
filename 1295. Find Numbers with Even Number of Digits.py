import math
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return sum( (int(math.log10(n)))%2 for n in nums)
