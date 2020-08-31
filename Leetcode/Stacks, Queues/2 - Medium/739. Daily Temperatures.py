class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        ls = [0] * len(T)
        buffer = deque()
        for ind,i in enumerate(T):
            while buffer and T[buffer[-1]]<i:
                t = buffer.pop()
                ls[t] = abs(t-ind)
            buffer.append(ind)
        return ls
