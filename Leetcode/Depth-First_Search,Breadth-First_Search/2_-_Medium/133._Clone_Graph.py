"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node==None:
            return None
        stack = deque()
        stack.append(node)
        d = {}
        res = None
        while stack:
            nd = stack.pop()
            if nd.val not in d:
                d[nd.val] = Node(nd.val)
            res = d[nd.val]
            for i in nd.neighbors:
                if i.val not in d:
                    d[i.val] = Node(i.val)
                    stack.append(i)
                res.neighbors.append(d[i.val])
        return d[1]