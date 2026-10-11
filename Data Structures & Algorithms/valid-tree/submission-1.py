class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlst = {i: [] for i in range(n)}

        for edge in edges:
            adjlst[edge[0]].append(edge[1])
            adjlst[edge[1]].append(edge[0])

        
        visited = set()
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for child in adjlst[node]:
                if child == prev: continue
                if not dfs(child, node):
                    return False
            return True

        if not dfs(0, None):
            return False

        return True and len(visited) == n
            