# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        depth = float("inf")
        stack = deque()
        stack.append((root, 1))
        while stack:
            node, level = stack.pop()
            if not node.left and not node.right:
                depth = min(level, depth)
            if node.left:
                stack.append((node.left, level+1))
            if node.right:
                stack.append((node.right, level+1))
        return depth