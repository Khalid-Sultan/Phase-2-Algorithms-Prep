# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        stack = deque()
        stack.append((root, 0))
        res = {}
        while stack:
            node, level = stack.pop()
            if level not in res:
                res[level] = []
            if level % 2 == 1 and node.val % 2 == 1:
                return False
            if level % 2 == 0 and node.val % 2 == 0:
                return False
            res[level].append(node.val)
            if node.right:
                stack.append((node.right, level + 1))
            if node.left:
                stack.append((node.left, level + 1))
        for level in res:
            check = level % 2
            for i in range(1, len(res[level])):
                if check == 0 and res[level][i] <= res[level][i - 1]:
                    return False
                if check == 1 and res[level][i] >= res[level][i - 1]:
                    return False
        return True

