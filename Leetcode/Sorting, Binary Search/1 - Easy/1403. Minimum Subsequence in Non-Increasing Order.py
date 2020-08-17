class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        t = [0]*100
        sums = 0
        for i in nums:
            t[i-1]+=1
            sums+=i
        ct = 0
        for ind, i in enumerate(t):
            while i>0:
                nums[ct] = ind+1
                ct+=1
                i-=1
        other_sum = nums[-1]
        sums -= other_sum
        lt = [nums[-1]]
        end = -2
        while other_sum<=sums:
            other_sum+=nums[end]
            sums-=nums[end]
            lt.append(nums[end])
            end-=1
        return lt