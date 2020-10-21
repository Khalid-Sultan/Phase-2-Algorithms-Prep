class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        left_g = left_s = 0
        ct = 0
        while left_g < len(g) and left_s < len(s):
            if s[left_s] >= g[left_g]:
                ct += 1
                left_s, left_g = left_s + 1, left_g + 1
            elif s[left_s] < g[left_g]:
                left_s += 1

        return ct