class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        
        # No Space Complexity
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if(nums[i]==nums[j]):
        #             count+=1   
        # return count
        
        dict = {}
        for i in nums:
            if i in dict:
                count+=dict[i]
                dict[i]+=1
            else:
                dict[i] = 1
        return count