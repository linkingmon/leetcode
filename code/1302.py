# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        node_list = [root]
        while True:
            next_node_list = []
            next_path_list = []
            for i in range(len(node_list)):
                if node_list[i].left is not None:
                    next_node_list.append(node_list[i].left)
                if node_list[i].right is not None:
                    next_node_list.append(node_list[i].right)
            if len(next_node_list) == 0:
                break
            node_list = next_node_list     
        sum_val = 0
        for i in range(len(node_list)):
            sum_val += node_list[i].val
        return sum_val