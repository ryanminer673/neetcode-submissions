# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # recursive dfs
        # save the depth at each node then check that they doffer by no more than 1
        is_balanced = True

        def dfs(head):

            nonlocal is_balanced

            if not head:
                return 0

            left_depth = dfs(head.left)
            right_depth = dfs(head.right)

            if left_depth > 1 + right_depth or left_depth < right_depth - 1:
                is_balanced = False

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return is_balanced

            
