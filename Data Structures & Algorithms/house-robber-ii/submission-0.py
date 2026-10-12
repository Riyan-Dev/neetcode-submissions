class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        n = len(nums)

        if not nums:
            return 0
        if n <= 2:
            return max(nums)

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i]+dp[i-2])
        
        return dp[-1]


