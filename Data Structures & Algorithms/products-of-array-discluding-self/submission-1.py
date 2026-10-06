class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zc = 1, 0
        for n in nums:
            if n:
                prod *= n
            else:
                zc += 1
        res = [0] * len(nums)
        if zc > 1: return res

        for i, n in enumerate(nums):
            if zc: res[i] = 0 if n else prod
            else:
                res[i] = prod // n
        
        return res

