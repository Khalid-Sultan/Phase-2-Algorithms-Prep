class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = {}
        for ind, i in enumerate(groupSizes):
            if i not in d:
                d[i] = [[ind]]
            else:
                if len(d[i][-1])==i:
                    d[i].append([ind])
                else:
                    d[i][-1].append(ind)
        res = []
        for i in d:
            res.extend(d[i])
        return res