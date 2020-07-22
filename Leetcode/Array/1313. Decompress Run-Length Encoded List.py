class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        count = 0       
        for i in range(0,len(nums),2):
            count += nums[i]
        l = [0] * count
        temp = 0
        j = 0
        ct = nums[j]
        pr = nums[j+1]
        for i in range(count):
            if temp==ct and j+2<len(nums):
                temp = 0
                j += 2
                ct = nums[j]
                pr = nums[j+1]
            l[i] = pr
            temp+=1
        return l
