class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        j = 0
        tmp = []
        for i in range(len(s)):
            
            while j < len(t):
                if s[i] == t[j]:
                    tmp.append(t[j])
                    j+=1
                    break
                j+=1
            
            if len(tmp) == len(s) : return True

        return False

