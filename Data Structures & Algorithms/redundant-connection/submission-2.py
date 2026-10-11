class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = {i: [] for i in range(1, n+1)}

        

        def dfs (node, par):
            if node in visited:
                return True

            visited.add(node)
            for child in adj[node]:
                if child == par:
                    continue
                if dfs(child, node):
                    return True


            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

            visited = set()
            if dfs(u, -1): return [u, v]




                
            
             
        


