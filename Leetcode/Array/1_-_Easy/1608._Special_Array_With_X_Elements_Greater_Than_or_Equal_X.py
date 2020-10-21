class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        res = prev = -1
        for ind, i in enumerate(nums):
            if i>=len(nums)-ind and len(nums)-ind>prev:
                print(nums, ind, i, prev)
                return len(nums)-ind
            prev=i
        return res