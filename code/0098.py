# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root):
            has_right = root.right is not None
            has_left = root.left is not None
            if has_right:
                right_bst, right_max, right_min = check(root.right)
            else:
                right_bst, right_max = True, root.val
            if has_left:
                left_bst, left_max, left_min = check(root.left)
            else:
                left_bst, left_min = True, root.val
            root_bst = ((not has_left) or left_max < root.val) and \
                        ((not has_right) or root.val < right_min)
            return left_bst and root_bst and right_bst, right_max, left_min
        [out_res, _, _] = check(root)
        return out_res