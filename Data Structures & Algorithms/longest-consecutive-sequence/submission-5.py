class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)

        longest = 0
        seen = set()

        for num in unique:
            lenght = 1
            if num in seen:
                continue
            while (num + lenght) in unique:
                lenght += 1
                seen.add(num + lenght -1)
            
            longest = max(lenght, longest)


        return longest