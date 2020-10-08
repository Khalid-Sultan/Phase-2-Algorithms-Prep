class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last_indices = [0] * 26
        for ind, i in enumerate(S):
            last_indices[ord(i) - 97] = ind

        start = 0
        end = last_indices[ord(S[start]) - 97]

        res = []
        while start < len(S) or end < len(S):
            found = False
            for i in range(start, end + 1):
                if last_indices[ord(S[i]) - 97] > end:
                    end = last_indices[ord(S[i]) - 97]
                    found = True
                    break
            if not found:
                res.append(end + 1 - start)
                start = end + 1
                if start >= len(S): break
                end = last_indices[ord(S[start]) - 97]
        return res


