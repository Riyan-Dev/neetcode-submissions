class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        l = len(nums)
        ans = [0] * len(nums)*2

        for i, n in enumerate(nums):
            ans[i] = ans[l+i] = n

        return ans