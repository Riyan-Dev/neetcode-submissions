class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            crs, pre = edge[0], edge[1]
            graph[crs].append(pre)

        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if graph[crs] == []:
                return True

            visited.add(crs)

            for pre in graph[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            graph[crs] = []
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
            


