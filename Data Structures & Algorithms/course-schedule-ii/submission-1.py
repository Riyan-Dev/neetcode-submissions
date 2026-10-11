class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        premap = {i: [] for i in range(numCourses)}

        for edge in prerequisites:
            premap[edge[0]].append(edge[1])
        res = []
        visited, cycle = set(), set()
        def dfs(crs):
            if crs in visited:
                return True
            if crs in cycle:
                return False

            cycle.add(crs)
            for pre in premap[crs]:
                if dfs(pre) == False:
                    return False

            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True


        for i in range(numCourses):
            if dfs(i) == False:
                return []
            
        return res