class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        

        sw = strs[0]
        i = 0
        while i < len(sw):
            for s in strs:
                if i < len(s) and sw[i] == s[i]:
                    continue
                else:
                    return sw[:i]
            i += 1

        return sw
        

        