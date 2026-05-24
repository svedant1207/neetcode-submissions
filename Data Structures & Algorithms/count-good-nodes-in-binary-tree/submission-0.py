# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return

        stk = [(root, root.val)]
        count = 0

        while stk:
            node, maxi = stk.pop()

            if node.val >= maxi:
                count += 1

            nmax = max(maxi, node.val)

            if node.right:
                stk.append((node.right, nmax))
            
            if node.left:
                stk.append((node.left, nmax))

        return count