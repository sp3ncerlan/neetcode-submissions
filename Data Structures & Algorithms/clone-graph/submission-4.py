"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # deep copy meaning we have to create new nodes
        og_to_clone = {} # { og node : cloned node }

        def dfs(node):
            if node in og_to_clone:
                return og_to_clone[node]

            clone = Node(node.val)
            og_to_clone[node] = clone

            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))

            return clone

        return dfs(node)