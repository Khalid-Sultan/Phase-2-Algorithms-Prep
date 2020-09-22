# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = deque()
        res = deque()
        stack.append((root, 1))
        while stack:
            node = stack.popleft()
            if len(res)<node[1]:
                res.append(node[0].val)
            else:
                res.append(max(res.pop(), node[0].val))
            if node[0].left:
                stack.append((node[0].left, node[1]+1))
            if node[0].right:
                stack.append((node[0].right, node[1]+1))
        return res