class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            if nums[abs(i)-1]<0:
                ret.append(abs(i))
            else:
                nums[abs(i)-1]*=-1
        return ret