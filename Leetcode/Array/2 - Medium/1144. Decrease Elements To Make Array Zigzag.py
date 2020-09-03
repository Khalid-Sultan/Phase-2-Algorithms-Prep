class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        t = [0] * len(nums)
        for ind, i in enumerate(nums): t[ind] = i
        return min(self.evenindexed(nums), self.oddindexed(t))        

    def evenindexed(self, nums: List[int])-> int:
        ctr = 0
        for i in range(0, len(nums), 2):
            if i+1<len(nums) and i-1>=0 and nums[i-1]<nums[i]>nums[i+1]:
                continue
            if i-1>=0 and nums[i-1]>=nums[i]:
                mx = abs(nums[i-1]-nums[i])+1
                nums[i-1]-=mx
                ctr+=mx
            if i+1<len(nums) and nums[i+1]>=nums[i]:
                mx = abs(nums[i+1]-nums[i])+1
                nums[i+1]-=mx
                ctr+=mx
        print(ctr)
        return ctr
    def oddindexed(self, nums: List[int])-> int:
        ctr = 0
        for i in range(1, len(nums), 2):
            if i+1<len(nums) and i-1>=0 and nums[i-1]<nums[i]>nums[i+1]:
                continue
            if i-1>=0 and nums[i-1]>=nums[i]:
                mx = abs(nums[i-1]-nums[i])+1
                nums[i-1] -= mx 
                ctr+=mx
            if i+1<len(nums) and nums[i+1]>=nums[i]:
                mx = abs(nums[i+1]-nums[i])+1
                nums[i+1] -= mx 
                ctr+=mx
        print(ctr)
        return ctr
