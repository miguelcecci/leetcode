# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.as_list = []
        self.in_order_traverse(self.root)
        self.list_pointer = 0
        print(self.as_list)
    
    def in_order_traverse(self, root):
        if root:
            self.in_order_traverse(root.left)
            self.as_list.append(root.val)
            self.in_order_traverse(root.right)

    def next(self) -> int:
        self.list_pointer = self.list_pointer+1
        return self.as_list[self.list_pointer-1]    

    def hasNext(self) -> bool:
        if self.list_pointer == len(self.as_list):
            return False
        return True

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
