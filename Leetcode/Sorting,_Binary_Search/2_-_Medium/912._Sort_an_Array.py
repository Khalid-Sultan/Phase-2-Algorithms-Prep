class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quickSort(nums, 0, len(nums)-1)
        return nums

    def quickSort(self, nums, start, end):
        if start>=end:
            return
        i,j = start + 1, end
        while i <= j:
            while i <= j and nums[i] <= nums[start]:
                i += 1
            while i <= j and nums[j] >= nums[start]:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[start], nums[j] = nums[j], nums[start]
        self.quickSort(nums, start, j-1)
        self.quickSort(nums, j+1, end)