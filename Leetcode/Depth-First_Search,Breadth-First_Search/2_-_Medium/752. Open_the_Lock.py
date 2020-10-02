class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        s = set(deadends)
        res = self.bfs(s, target)
        return res

    def bfs(self, deadends, target):
        res = 10000
        queue = deque()
        queue.append(([0, 0, 0, 0], 0))
        visited = set()
        while queue:
            node, count = queue.popleft()
            check = "{0:0=4d}".format(int("".join(map(str, node))))
            if check in deadends or check in visited:
                continue
            if check == target:
                res = min(res, count)
            # print(check, count)
            visited.add(check)
            for ind, i in enumerate(node):
                if i == 0:
                    # increment to 1
                    temp = node[:ind] + [1] + node[ind + 1:]
                    queue.append((temp, count + 1))
                    # decrement to 9
                    temp = node[:ind] + [9] + node[ind + 1:]
                    queue.append((temp, count + 1))
                elif i == 9:
                    # increment to 0
                    temp = node[:ind] + [0] + node[ind + 1:]
                    queue.append((temp, count + 1))
                    # decrement to 8
                    temp = node[:ind] + [8] + node[ind + 1:]
                    queue.append((temp, count + 1))
                else:
                    # increment by 1
                    temp = node[:ind] + [i + 1] + node[ind + 1:]
                    queue.append((temp, count + 1))
                    # decrement by 1
                    temp = node[:ind] + [i - 1] + node[ind + 1:]
                    queue.append((temp, count + 1))
        return -1 if res == 10000 else res