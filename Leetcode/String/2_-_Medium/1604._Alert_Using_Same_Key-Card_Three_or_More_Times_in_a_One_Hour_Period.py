from datetime import datetime


class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        FMT = '%H:%M'
        z = list(zip(keyName, keyTime))
        z.sort(key=lambda x: x[1])
        res = set()
        d = {}

        for i in z:
            if i[0] not in d:
                d[i[0]] = deque()
            d[i[0]].append(i[1])
        for key in d:
            for ind, time in enumerate(d[key]):
                ct = 1
                for ind2 in range(ind + 1, len(d[key])):
                    tdelta = datetime.strptime(d[key][ind2], FMT) - datetime.strptime(time, FMT)
                    if tdelta.total_seconds() <= 3600:
                        ct += 1
                    if ct == 3:
                        res.add(key)
                        break
        return sorted(list(res))