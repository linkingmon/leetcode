# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        node_list = [root]
        path_list = [0]
        layer = 0
        while True:
            next_node_list = []
            next_path_list = []
            for i in range(len(node_list)):
                if node_list[i].left is not None:
                    next_node_list.append(node_list[i].left)
                    next_path_list.append(path_list[i]<<1)
                if node_list[i].right is not None:
                    next_node_list.append(node_list[i].right)
                    next_path_list.append((path_list[i]<<1)+1)
            if len(next_node_list) == 0:
                break
            layer = layer + 1
            node_list = next_node_list     
            path_list = next_path_list
        deep_path = path_list[0]
        max_deep = 0
        for i in range(1,len(path_list)):
            deep = floor(log2(deep_path^path_list[i])) + 1
            if deep > max_deep:
                max_deep = deep
        for i in range(layer-1,max_deep-1,-1):
            root = root.left if (deep_path & (1 << i) == 0) else root.right
        return root