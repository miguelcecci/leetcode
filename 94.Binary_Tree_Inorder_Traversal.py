# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        result = []

        def recursive_traversal(node):

            if node != None:
                recursive_traversal(node.left)

                result.append(node.val)

                recursive_traversal(node.right)
        
        recursive_traversal(root)

        return result
                
        
