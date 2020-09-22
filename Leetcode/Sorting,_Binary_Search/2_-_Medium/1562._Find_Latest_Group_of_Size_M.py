class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        if (len(arr) == 1): return 1
        res = [[0 for i in range(2)]] * len(arr)
        mx = -1
        for ind, i in enumerate(arr):
            i -= 1
            # Current Element
            current = res[i]
            prev = nxt = 0
            # Last element of previous sequence
            if i - 1 > -1 and res[i - 1][0] == 1:
                prev = res[i - 1][1]
            # first element and last element of next sequence
            if i < len(res) - 1 and res[i + 1][0] == 1:
                nxt = res[i + 1][1]

            res[i] = [1, prev + nxt + 1]
            if i - 1 > -1 and res[i - 1][0] == 1:
                if res[i - 1][1] == m or res[i - res[i - 1][1]][1] == m:
                    mx = max(ind, mx)
                res[i - res[i - 1][1]][1] = res[i][1]
                res[i - 1][1] = res[i][1]
            if i < len(res) - 1 and res[i + 1][0] == 1:
                if res[i + 1][1] == m or res[i + res[i + 1][1]][1] == m:
                    mx = max(ind, mx)
                res[i + res[i + 1][1]][1] = res[i][1]
                res[i + 1][1] = res[i][1]
            if res[i][1] == m:
                mx = max(ind + 1, mx)
        return mx