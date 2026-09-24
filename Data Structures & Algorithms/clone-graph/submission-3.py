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

        visited = set()
        def dfs(node):
            visited.add(node)
            og_to_clone[node] = Node(node.val)

            for nei in node.neighbors:
                if nei not in visited:
                    dfs(nei)

        dfs(node)

        # connect
        for og, clone in og_to_clone.items():
            for nei in og.neighbors:
                clone.neighbors.append(og_to_clone[nei])

        return og_to_clone[node]