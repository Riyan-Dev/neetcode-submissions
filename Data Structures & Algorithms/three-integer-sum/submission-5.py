class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hm = defaultdict(tuple)
        for i, n in enumerate(nums):
            pairs = twoSum(nums, i, (n*-1))
            for p in pairs:
                p.append(n)
                p.sort()
                hm[tuple(p)] = p

        return list(hm.values())        



def twoSum(nums, x, target):
    res = []
    l, r = 0, len(nums) - 1

    while l < r:
        if l == x:
            l += 1
            continue
        if r == x:
            r -= 1
            continue

        if nums[l] + nums[r] == target:
            res.append([nums[l], nums[r]])
            r -= 1
        elif nums[l] + nums[r] > target:
            r -= 1
        else:
            l += 1
    
    return res
