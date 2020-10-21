class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        res = []
        for i in nums:
            if not res:
                res.append([i, 1])
            else:
                found = False
                for j in range(len(res) - 1, -1, -1):
                    if res[j][0] == i:
                        continue
                    elif res[j][0] == i - 1:
                        res[j][0] = i
                        res[j][1] += 1
                        found = True
                        break
                if not found:
                    res.append([i, 1])
        ct = 0
        for i in res:
            if i[1] < 3:
                return False
            ct += i[1]
        return ct == len(nums)
