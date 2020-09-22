class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(0, len(nums)):
            j = target - nums[i]
            if j in d:
                return [d[j], i]
            d[nums[i]] = i
