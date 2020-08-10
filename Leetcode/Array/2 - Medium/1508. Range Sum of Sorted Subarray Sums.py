class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        ret = [nums[0]]
        for i in range(1, len(nums)):
            ret.append(ret[-1] + nums[i])
        
        prev = [i for i in ret]
        for i in range(1, len(nums)):
            l = []
            for j in range(1, len(prev)):
                 l.append(prev[j] - prev[0])   
            ret = ret + l
            prev = l
        
        ret.sort()
        ret = ret[left-1: right]
        return sum(ret) % (pow(10,9)+7)
        