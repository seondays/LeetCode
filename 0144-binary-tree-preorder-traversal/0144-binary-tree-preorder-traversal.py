# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        mystack = []
        
        while root or mystack:
            if root:
                result.append(root.val)
                mystack.append(root.right)
                root = root.left
            else:
                root = mystack.pop()
        
        return result