# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Iterative solution -
    #      Space - O(n) for iterating over the whole tree
    #      Time - O(n) for iterating over the whole tree
    # Recursive solution -
    #      Space - O(n) for iterating over the whole tree
    #      Time - O(n) for iterating over the whole tree

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        disjoints = []
        to_delete = set(to_delete)
        # self.delNodesIter(root, to_delete, disjoints)
        self.delNodesRecur(root, to_delete, disjoints, True)
        return disjoints

    def delNodesIter(self, root: TreeNode, to_delete: set, disjoints: List[TreeNode]) -> List[TreeNode]:
        # Helper function to store disjoint children of deleted node
        def addToDisjoints(node, to_delete, disjoints):
            if node and node.val not in to_delete:
                disjoints.append(node)

        queue = deque()

        # Add root to disjoint list if root.val is in the list of items to be deleted
        queue.append([root, True])
        if root.val not in to_delete:
            queue[-1][1] = False
            disjoints.append(root)

        while queue:
            node, brokenOff = queue.popleft()

            # If node is removed, check if the children are to be removed or not
            if brokenOff:
                addToDisjoints(node.left, to_delete, disjoints)
                addToDisjoints(node.right, to_delete, disjoints)

            if node.left:
                queue.append([node.left, False])
                if node.left.val in to_delete:
                    queue[-1][1] = True
                    node.left = None

            if node.right:
                queue.append([node.right, False])
                if node.right.val in to_delete:
                    queue[-1][1] = True
                    node.right = None

        return disjoints

    def delNodesRecur(self, node: TreeNode, to_delete: set, disjoints: List[TreeNode], deleted: bool) -> List[TreeNode]:
        if not node:
            return None
        # If node is to be deleted pass that information on to the children
        if node.val in to_delete:
            node.left = self.delNodesRecur(node.left, to_delete, disjoints, True)
            node.right = self.delNodesRecur(node.right, to_delete, disjoints, True)
            return None
        else:
            # If deleted, add the new node to the result set and continue
            if deleted:
                disjoints.append(node)
            node.left = self.delNodesRecur(node.left, to_delete, disjoints, False)
            node.right = self.delNodesRecur(node.right, to_delete, disjoints, False)
            return node