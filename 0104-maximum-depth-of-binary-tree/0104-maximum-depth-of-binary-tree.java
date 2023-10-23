/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int dp(TreeNode root) {
        int left;
        int right;

            if (root == null) {
                return 0;
            }

            left = dp(root.left);
            right = dp(root.right);

            return Integer.max(left, right) + 1;
        }

    public int maxDepth(TreeNode root) {
        return dp(root);
    }
}