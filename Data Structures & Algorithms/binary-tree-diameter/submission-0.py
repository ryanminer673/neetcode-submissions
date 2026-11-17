# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        #i need to save the max (diamater) and count the sum if left and right node depth though
        
        best = 0

        def dfs(head):

            nonlocal best

            if not head:
                return 0

            # count teh max depth between the left and right root 
            left_depth = dfs(head.left)
            right_depth = dfs(head.right)

            best = max(best, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)

        return best
            


            