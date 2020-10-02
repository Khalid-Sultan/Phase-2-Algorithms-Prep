class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        count = 'x'
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    self.dfs(A, i, j, count)
                    count = 'y'
        res = 100000
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 'x':
                    found = self.search(A, i, j)
                    res = min(res, found)
        return res - 1

    def dfs(self, A, row, col, replacement):
        if row < 0 or col < 0 or row >= len(A) or col >= len(A[0]) or A[row][col] == 0 or A[row][col] == replacement:
            return
        A[row][col] = replacement
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in directions:
            self.dfs(A, row + i[0], col + i[1], replacement)

    def search(self, A, row, col):
        queue = deque()
        visited = set()
        queue.append((row, col, 0))
        visited.add((row, col))
        level = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while queue:
            i, j, level = queue.popleft()
            if i < 0 or j < 0 or i >= len(A) or j >= len(A[0]):
                continue
            if A[i][j] == 'x' and level > 0:
                continue
            if A[i][j] == 'y':
                return level
            for x in directions:
                if (i + x[0], j + x[1]) not in visited:
                    queue.append((i + x[0], j + x[1], level + 1))
                    visited.add((i + x[0], j + x[1]))
        return 100000
