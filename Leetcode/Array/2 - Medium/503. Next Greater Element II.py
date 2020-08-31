class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        buffer = deque()
        n = len(nums)
        res = [-1] * n
        for i in range(n*2):
            while buffer and nums[buffer[-1]]<nums[i%n]:
                res[buffer.pop()] = nums[i%n]
            if i<n:
                buffer.append(i)
        return res