# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p,q):
            if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val):
                return root
            else:
                if root.val > p.val:
                    return dfs(root.left,p,q)
                else:
                    return dfs(root.right,p,q)
        
        return dfs(root,p,q)