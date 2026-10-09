class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(sub, i, total):
            if total == target:
                res.append(sub.copy())
                return
            if i >= len(nums) or total > target:
                return


            sub.append(nums[i])
            dfs(sub, i, total + nums[i])
            sub.pop()
            dfs(sub, i+1, total)


        dfs([], 0, 0)

        
        return res

