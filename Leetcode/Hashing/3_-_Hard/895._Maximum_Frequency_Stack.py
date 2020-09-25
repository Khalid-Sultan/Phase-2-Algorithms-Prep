from heapq import *

class FreqStack:
    def __init__(self):
        self.counts = {}
        # self.maxes = deque()
        # self.stack = deque()
        self.stack = []
        self.counter = 1

    def push(self, x: int) -> None:
        if x not in self.counts:
            self.counts[x] = 0
        self.counts[x]+=1
        # self.stack.append(x)
        heappush(self.stack, (-1 * self.counts[x], -1 * self.counter, x))
        self.counter+=1

    def pop(self) -> int:
        # mx = 0
        # for i in self.counts:
        #     mx = max(self.counts[i], mx)
        # queue = deque()
        # while self.counts[self.stack[-1]]!=mx:
        #     queue.appendleft(self.stack.pop())
        # ret = self.stack.pop()
        # self.counts[ret]-=1
        # while queue:
        #     val = queue.popleft()
        #     self.stack.append(val)
        # return ret
        count, index, val = heappop(self.stack)
        self.counts[val]-=1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()