# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = deque()
        d = dict()
        res = deque()
        stack.append((root, 1))
        while stack:
            node, level = stack.pop()
            if level not in d:
                d[level] = deque()
            d[level].append(node.val)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        for i in d:
            res.appendleft(d[i])
        return res
