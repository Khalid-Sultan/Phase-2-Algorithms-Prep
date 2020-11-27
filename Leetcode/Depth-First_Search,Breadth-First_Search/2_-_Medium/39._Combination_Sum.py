class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, temporary, start, target):
            if target == 0:
                res.append(temporary)
            for i in range(start, len(candidates)):
                if candidates[i] > target:
                    break
                dfs(candidates, temporary + [candidates[i]], i, target - candidates[i])

        candidates.sort()
        res = []
        dfs(candidates, [], 0, target)
        return res
