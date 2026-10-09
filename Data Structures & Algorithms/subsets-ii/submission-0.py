class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs (sub, i, n):
            if i >= n:
                res.append(sub.copy())
                return
            
            sub.append(nums[i])
            dfs(sub, i+1, n)
            sub.pop()

            while i < n-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(sub,i+1,n)

        dfs([], 0, len(nums))
        return res

        