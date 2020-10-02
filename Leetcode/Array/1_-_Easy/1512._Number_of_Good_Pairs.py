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

    #     d = {}
    #     count = 0
    #     for i in nums:
    #         if i not in d:
    #             d[i] = 0
    #         else:
    #             d[i] += 1
    #     count = 0
    #     for i in d:
    #         count += self.summate(d[i])
    #     return count
    #
    # def summate(self, n):
    #     return (n ** 2 + n) // 2