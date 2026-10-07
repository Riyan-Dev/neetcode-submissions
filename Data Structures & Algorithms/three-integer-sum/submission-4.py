class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        hashmap = defaultdict(tuple)
        for i, n in enumerate(nums):
            twos = twoSum(nums, i, (n*-1))
            if twos:
                for pair in twos:
                    pair.append(n)
                    tripple = sorted(pair)
                    hashmap[tuple(tripple)] = tripple
        
        return list(hashmap.values())


def twoSum(nums: List[int], x: int, target: int):
    l, r = 0, len(nums) -1
    res = []
    while l < r:
        if l == x:
            l += 1
            continue
        elif r == x:
            r -= 1
            continue
        if nums[l] + nums[r] == target:
            res.append([nums[l], nums[r]])
            r -= 1
        elif nums[l] + nums[r] < target:
            l += 1
        else:
            r -= 1
    
    return res