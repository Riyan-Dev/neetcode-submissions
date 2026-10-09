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
            return
        seen = []
        seen.append(node)
        newNode = Node(node.val)
        mp = {newNode.val: newNode}

        def dfs(n, new):
            if not n:
                return
            
            for i in n.neighbors:
                if i not in seen:
                    newChild = Node(i.val)
                    seen.append(i)
                    mp[i.val] = newChild
                    dfs(i, newChild)
                    new.neighbors.append(newChild)
                else:
                    new.neighbors.append(mp.get(i.val))
                

        dfs(node, newNode)
        return newNode