class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(sub, i, n):
            if i >= n:
                res.append(sub.copy())
                return

            for num in nums:
                if num not in sub:  
                    sub.append(num)
                    dfs(sub, i+1, n)
                    sub.pop()

            
        dfs([], 0, len(nums))
        return res