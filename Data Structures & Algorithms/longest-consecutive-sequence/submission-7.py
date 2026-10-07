class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        ul = sorted(list(set(nums)))
        longest = 1
        count = 1
        i = 0
        print(ul)
        while i+1 < len(ul):
            if (ul[i] + 1) == ul[i+1]:
                count += 1
            else:
                longest = max (count, longest)
                count = 1
            i += 1

        return max(longest, count)