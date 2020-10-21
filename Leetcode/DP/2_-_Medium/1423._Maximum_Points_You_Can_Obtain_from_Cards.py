class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        s = sum(cardPoints[-k:])
        mx = s
        prev = 0
        nx = 0
        for i in range(k):
            prev += cardPoints[i]
            nx += cardPoints[-k+i]
            t = prev + s - nx
            mx = max(mx, t)
        return mx