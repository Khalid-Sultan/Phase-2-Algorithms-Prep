class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.length = len(times)
        self.aggregate = {}
        self.maxes = []
        ls = mx = 0
        for i in range(self.length):
            if self.persons[i] not in self.aggregate:
                self.aggregate[self.persons[i]] = 0
            self.aggregate[self.persons[i]] += 1
            if self.aggregate[self.persons[i]]>=mx:
                mx = max(mx, self.aggregate[self.persons[i]])
                ls = self.persons[i]
            self.maxes.append(ls)
    def q(self, t: int) -> int:
        l,r = 0, self.length
        while l<r:
            m = l + (r-l)//2
            if self.times[m]>t:
                r = m
            else:
                l = m+1
        return self.maxes[l-1]
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)