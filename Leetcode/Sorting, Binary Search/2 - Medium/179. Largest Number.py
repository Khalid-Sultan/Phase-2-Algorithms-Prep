import functools
from collections import deque


class Solution:
    def compare(self, num1, num2):
        num1, num2 = str(num1), str(num2)
        if num1[0] < num2[0]:
            return -1
        elif num1[0] > num2[0]:
            return 1
        else:
            if len(num1) == len(num2):
                return 1 if int(num1) >= int(num2) else -1
            a, b = int(num1 + num2), int(num2 + num1)
            if a <= b: return -1
            return 1

    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1: return str(nums[0])
        nums = sorted(nums, key=functools.cmp_to_key(self.compare))
        s = deque()
        for i in range(len(nums) - 1, -1, -1):
            s.append(str(nums[i]))
        while s and s[0] == "0":
            s.popleft()
        if not s: return "0"
        return "".join(s)
