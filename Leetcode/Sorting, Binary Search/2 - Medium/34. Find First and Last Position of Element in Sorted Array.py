class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l,r = 0, len(nums)-1
        res = [-1,-1]
        if len(nums)==0:
            return res
        while l<r:
            m = l + (r-l)//2
            if nums[m]>=target:
                r = m
            else:
                l = m+1
        if nums[l]==target:
            res[0] = l
        else:
            return res

        r = len(nums)-1
        while(l<r):
            m = 1 + l + (r-l)//2
            if nums[m]<=target:
                l = m
            else:
                r = m-1
        if nums[r]==target:
            res[1] = r
            return res
        else:
            return [-1,-1]
