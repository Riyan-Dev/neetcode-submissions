class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        lenmax = 0
        cur = 0
        for n in nums:
            if n == 1:
                cur += 1
            else:
                lenmax = max(cur, lenmax)
                cur = 0
        return max(cur, lenmax)