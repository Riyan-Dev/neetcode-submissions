class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        nj = i
        while i >= 0:
            if nums[i] == 0:
                i -= 1
                continue
            if i + nums[i] >= nj:
                nj = i
            i -= 1
            
        return nj == 0
        

            