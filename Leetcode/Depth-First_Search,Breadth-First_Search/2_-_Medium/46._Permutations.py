class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #     s = set(nums)
        #     total = []
        #     count = len(s)
        #     for i in nums:
        #         self.recur(s, nums, set([i]), count, [], total)
        #     return total
        # def recur(self, s, nums: List[int], visited, count, res, total):
        #     if count==1:
        #         diff = list(s^set(res))[0]
        #         total.append(res+[diff])
        #         return
        #     for i in nums:
        #         if i not in visited:
        #             self.recur(s, nums, visited|{i}, count-1, res+[i], total)
        #     return

        def dfs(nums, res, temp, visited):
            if len(temp) == len(nums):
                res.append(temp)
                return
            for i in nums:
                if i not in visited:
                    visited.add(i)
                    dfs(nums, res, temp + [i], visited)
                    visited.remove(i)

        res = []
        dfs(nums, res, [], set())
        return res
