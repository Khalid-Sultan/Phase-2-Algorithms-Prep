# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: TreeNode):
        stack = deque()
        self.res = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            self.res.append(root.val)
            root = root.right
        self.counter = -1

    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.counter += 1
        return self.res[self.counter]

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.counter + 1 < len(self.res)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()