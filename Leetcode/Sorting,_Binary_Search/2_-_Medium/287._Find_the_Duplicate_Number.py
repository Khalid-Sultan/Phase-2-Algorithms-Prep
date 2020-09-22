class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        for ind,i in enumerate(nums):
            l,r = ind+1, len(nums)-1
            while l<=r:
                m = l + (r-l)//2
                if nums[m]==i:
                    return i
                elif nums[m]<i:
                    l = m+1
                else:
                    r = m-1
        return -1
