class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        for ind, i in enumerate(words):
            for ind2, j in enumerate(words):
                if ind==ind2: continue
                if i in j:
                    res.append(i)
                    break
        return res