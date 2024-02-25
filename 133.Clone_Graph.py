"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        created = {}
        def clone_node(node):
            if node == None:
                return None

            if node.val in created:
                return created[node.val]
            
            clone = Node(node.val)
            created[node.val] = clone

            for i in node.neighbors:
                clone.neighbors.append(clone_node(i))
            return clone

        return clone_node(node)
