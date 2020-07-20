class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        returnList = [0] * len(nums)
        temp = 0
        for i in range(0,n):
            returnList[temp] = nums[i]
            returnList[temp+1] = nums[n]
            n+=1
            temp+=2
        return returnList
            
        