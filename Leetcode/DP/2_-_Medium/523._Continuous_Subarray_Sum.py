class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if k==0:
#                     if nums[i:j+1].count(0)==j-i+1:
#                         return True
#                 elif sum(nums[i:j+1])%k==0:
#                     return True
#         return False

        tracker = {}
        tracker[0] = -1
        cumulative = 0
        for ind, i in enumerate(nums):
            cumulative += i
            divisible = cumulative
            if k!=0:
                divisible = cumulative % k
            if divisible in tracker:
                if abs(tracker[divisible] - ind)>=2:
                    return True
            else:
                tracker[divisible] = ind
            print(cumulative, divisible, ind, i)
            cumulative = divisible
        return False