class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        s = 0
        last = len(piles)-2
        for i in range(len(piles)//3):
            s+=piles[last]
            last-=2
        return s