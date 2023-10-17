# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dsf(node):
            if not node:
                return -1
            
            left = dsf(node.left)
            right = dsf(node.right)

            self.diameter = max(self.diameter,left + right + 2)
            return max(left,right) + 1
        
        dsf(root)
        return self.diameter
        