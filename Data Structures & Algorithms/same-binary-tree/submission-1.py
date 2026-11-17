# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if not p and not q:
            return True
        if not p and q:
            return False
        if not q and p:
            return False
        
        queue1 = deque()
        queue2 = deque()

        queue1.append(p)
        queue2.append(q)

        while queue1 or queue2:

            node1 = queue1.popleft()
            node2 = queue2.popleft()

            if node1.val != node2.val:
                return False

            if not node1.left and node2.left:
                return False
            if not node1.right and node2.right:
                return False
            if not node2.left and node1.left:
                return False
            if not node2.right and node1.right:
                return False

            if node1.left:
                queue1.append(node1.left)
            if node1.right:
                queue1.append(node1.right)

            if node2.left:
                queue2.append(node2.left)
            if node2.right:
                queue2.append(node2.right)

        if not queue1 and not queue2:
            return True
        return False
            

