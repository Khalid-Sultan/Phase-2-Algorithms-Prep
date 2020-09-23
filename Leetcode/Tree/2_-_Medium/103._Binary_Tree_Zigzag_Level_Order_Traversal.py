# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        dic = {}
        stack = deque()
        stack.append((root, 1))
        while stack:
            node, level = stack.pop()
            if not node:
                continue
            if not level in dic:
                dic[level] = deque()
            if level % 2 == 0:
                dic[level].append(node.val)
            else:
                dic[level].appendleft(node.val)
            stack.append((node.left, level + 1))
            stack.append((node.right, level + 1))
        return dic.values()
