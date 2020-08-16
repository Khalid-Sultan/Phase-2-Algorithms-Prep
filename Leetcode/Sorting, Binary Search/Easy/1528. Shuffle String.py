class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = ['']*len(indices)
        for ind,i in enumerate(indices):
            res[i] = s[ind]
        return "".join(res)