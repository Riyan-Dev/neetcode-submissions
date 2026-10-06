class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        for s in strs:
            ht = [0] * 26
            for c in s:
                ht[ord(c) - ord('a')] += 1
            res[tuple(ht)].append(s)
        return list(res.values())