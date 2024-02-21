# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        # 만약에 root가 null이면 하여튼 left right 이런 걸 참조하면 안됨
        if root:
            result += self.inorderTraversal(root.left)

            result.append(root.val)

            result += self.inorderTraversal(root.right)

        return result