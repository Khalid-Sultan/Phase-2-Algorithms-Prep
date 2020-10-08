from heapq import *


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for i in stones:
            heappush(h, -1 * i)

        while len(h) > 1:
            last = (heappop(h) * -1) - (heappop(h) * -1)
            heappush(h, -1 * last)
        return -1 * heappop(h)