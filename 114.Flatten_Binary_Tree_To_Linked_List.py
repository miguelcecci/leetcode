# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        result = []

        def rec(root):
            if root != None:
                result.append(root.val)
                rec(root.left)
                rec(root.right)
            
        rec(root)

        asdf = None
        for i in range(len(result)-1, -1, -1):
            asdf = TreeNode(val=result[i], left=None, right=asdf)
        
        if root != None:
            root.right = asdf.right
            root.left = None
            
        return root
