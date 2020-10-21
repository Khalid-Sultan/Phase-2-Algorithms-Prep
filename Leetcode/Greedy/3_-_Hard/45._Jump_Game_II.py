class Solution:
    def jump(self, nums: List[int]) -> int:
        ct = 0
        i = 0
        while i < len(nums) - 1:
            mx = 0
            mx_2 = 0
            for j in range(i + 1, i + nums[i] + 1):
                if j >= len(nums) - 1:
                    mx_2 = j
                    break
                if j + nums[j] >= mx:
                    mx = j + nums[j]
                    mx_2 = j
            i = mx_2
            ct += 1
        return ct
