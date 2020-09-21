class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        d = {}
        for i in edges:
            head, tail = min(i[0],i[1]), max(i[0],i[1])
            if head not in d:
                d[head] = deque()
            d[head].append(tail)
        print(d)
        return self.recur(target, 1, 1, d, t)[1]
    def recur(self, target, current, probability, paths, t):
        # print(current, t, probability)
        if t<0:
            return False, 0
        if current==target:
            if t==0: return True, probability
            elif current in paths: return False, 0
            else:
                return True, probability
        if current not in paths:
            return False, 0
        x = probability * (1/len(paths[current]))
        for i in paths[current]:
            check, prob = self.recur(target, i, x, paths, t-1)
            # print(check, prob)
            if check==True:
                return True, prob
        if current==target:
            return True, x
        return False, 0