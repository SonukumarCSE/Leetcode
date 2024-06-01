# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        q = deque()
        maxw = 0
        q.append((root,0))
        while q:
            size = len(q)
            left = q[0][1]
            right = q[-1][1]
            maxw = max(maxw, right - left + 1)
            for i in range(size):
                node, idx = q.popleft()
                if node.left:
                    q.append((node.left,2*idx + 1))
                if node.right:
                    q.append((node.right, 2*idx + 2))
        return maxw