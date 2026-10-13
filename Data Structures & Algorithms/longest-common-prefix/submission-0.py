class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        strs.sort(key=len)

        sw = strs[0]
        i = 0
        while i < len(sw):
            for s in strs:
                if sw[i] == s[i]:
                    continue
                else:
                    return sw[:i]
            i += 1

        return sw
        

        