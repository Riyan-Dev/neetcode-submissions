class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cache = [-1] * n
        cache[n-1], cache[n-2] = cost[n-1], cost[n-2]
        def dfs(i):
            if i >= n:
                return 0
            if cache[i] != -1:
                return cache[i]

            cache[i] = min(dfs(i+1)+cost[i], dfs(i+2)+cost[i])

            return cache[i]

        return min(dfs(0), dfs(1))
