class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(nums, sub, dept, n):
            nonlocal res
            if dept >= n:
                res.append(sub)
                return 
            dfs(nums, sub + [nums[dept]], dept+1, n)
            dfs(nums, sub, dept+1, n)

        dfs(nums, [], 0, len(nums))

        return res
