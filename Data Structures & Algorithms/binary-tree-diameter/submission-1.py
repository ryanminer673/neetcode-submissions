# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        best_diam = 0

        def dfs(head):

            nonlocal best_diam

            if not head:
                return 0

            left_dist = dfs(head.left)
            right_dist = dfs(head.right)

            best_diam = max(best_diam, left_dist + right_dist)

            return 1 + max(left_dist, right_dist)

        dfs(root)

        return best_diam