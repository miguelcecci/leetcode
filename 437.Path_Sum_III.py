# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        results = []

        def recursive_search(root, target: int, root_sum: int, history: str) -> None:
            if root != None:
                root_sum_buffer = root.val + root_sum
                print(root_sum_buffer)
                if root_sum_buffer == target:
                    results.append(history)
                recursive_search(root.left, target, root_sum_buffer, history+'l')
                recursive_search(root.right, target, root_sum_buffer, history+'r')

                if history == '':
                    recursive_search(root.right, target, 0, '')
                    recursive_search(root.left, target, 0, '')

        recursive_search(root, targetSum, 0, '')
        return len(results)
