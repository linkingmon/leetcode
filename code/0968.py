# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def find(root):
            if root == None:
                return 2 # has covered but have no camera
            l_search = find(root.left)
            r_search = find(root.right)
            if l_search == 0 or r_search == 0:
                self.ans += 1
                return 1 # put camera
            if l_search == 1 or r_search == 1:
                return 2
            return 0 # no camera and is not covered
        # greedy from leaf nodes
        self.ans = 0
        root_state = find(root)
        return self.ans+1 if root_state == 0 else self.ans