class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<r:
            m = l + (r-l)//2
            if nums[r]>nums[m]:
                r = m
            else:
                l = m+1
        pivot = l
        l,r = 0, len(nums)
        while l<=r:
            mid = (pivot +( l + (r-l)//2 )) %len(nums)
            if nums[mid]<target:
                l = 1 + l + (r-l)//2
            elif nums[mid]>target:
                r = -1 + l + (r-l)//2
            else:
                return mid
        print(pivot)
        return -1
