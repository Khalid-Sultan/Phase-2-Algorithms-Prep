class Solution:
    def reorganizeString(self, S: str) -> str:
        d = {}
        for i in S:
            if i not in d:
                d[i] = 0
            d[i] -= 1
        h = list(zip(d.values(), d.keys()))
        heapify(h)
        res = [''] * len(S)
        while h:
            count, key = heappop(h)
            did = False
            if res[0] == '':
                res[0] = key
                did = not did
            else:
                for i in range(1, len(S)):
                    if res[i] == '' and res[i - 1] != key:
                        res[i] = key
                        did = not did
                        break
            if not did:
                return ""
            if count < -1:
                heappush(h, (count + 1, key))
        return "".join(res)



