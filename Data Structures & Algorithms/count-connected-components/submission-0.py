class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i:[] for i in range(n)}

        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        visited = set()
        def dfs(node):
            if node in visited:
                return

            visited.add(node)
            for child in adj[node]:
                dfs(child)

        count = 0
        for i in range(n):
            if i in visited: continue
            dfs(i)
            count+=1
        return count