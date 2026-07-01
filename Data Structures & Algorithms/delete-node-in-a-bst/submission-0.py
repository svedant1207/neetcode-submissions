# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        if root.val < key:
            root.right = self.deleteNode(root.right, key)

        elif root.val > key:
            root.left = self.deleteNode(root.left, key)

        else:
            if root.left is None and root.right is None:
                return 
            
            if root.left is None:
                return root.right
            
            if root.right is None:
                return root.left

            temp = self.find_min(root.right)
            root.val = temp.val
            root.right = self.deleteNode(root.right, temp.val) 

        return root


    def find_min(self, root):
        while root.left:
            root = root.left

        return root

            


        