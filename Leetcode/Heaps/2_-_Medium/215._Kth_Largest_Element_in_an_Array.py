from heapq import *
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        res = []
        for i in nums:
            heappush(res, -i)
        ans = 0
        while k>0:
            ans = heappop(res)
            k-=1
        return ans*-1