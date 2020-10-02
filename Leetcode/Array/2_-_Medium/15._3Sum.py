class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = deque()
        s = set()
        visited = set()
        for ind, i in enumerate(nums):
            d = {}
            if i in visited: continue
            visited.add(i)
            for ind2 in range(ind+1, len(nums)):
                j = nums[ind2]
                if -1 * j in d:
                    temp = sorted([d[-1 * (j)][0], d[-1 * (j)][1], j])
                    temp = "".join(str(k) for k in temp)
                    if temp in s: continue
                    s.add(temp)
                    res.append([d[-1 * (j)][0], d[-1 * (j)][1], j])
                else:
                    d[i+j] = [i,j]
        return res