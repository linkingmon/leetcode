# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        node_list = [root]
        path_list = [0]
        layer = 0
        p_path = None
        q_path = None
        p_deep = -1
        q_deep = -1
        while True:
            next_node_list = []
            next_path_list = []
            for i in range(len(node_list)):
                if node_list[i].left is not None:
                    next_node_list.append(node_list[i].left)
                    next_path_list.append(path_list[i])
                    if node_list[i].left == p:
                        p_path = path_list[i]
                        p_deep = layer
                    if node_list[i].left == q:
                        q_path = path_list[i]
                        q_deep = layer
                if node_list[i].right is not None:
                    next_node_list.append(node_list[i].right)
                    next_path_list.append(path_list[i]+2**layer)
                    if node_list[i].right == p:
                        p_path = path_list[i]+2**layer
                        p_deep = layer
                    if node_list[i].right == q:
                        q_path = path_list[i]+2**layer
                        q_deep = layer
            if len(next_node_list) == 0 or (p_path is not None and q_path is not None):
                break
            layer = layer + 1
            node_list = next_node_list     
            path_list = next_path_list
        min_deep = min(p_deep,q_deep)
        if min_deep == -1:
            return root
        out_node = root
        bit_and = 1
        for i in range(min_deep+1):
            p_dir = bit_and & p_path
            q_dir = bit_and & q_path
            if p_dir != q_dir:
                break
            out_node = out_node.left if p_dir == 0 else out_node.right
            bit_and = bit_and << 1
        return out_node
            
            