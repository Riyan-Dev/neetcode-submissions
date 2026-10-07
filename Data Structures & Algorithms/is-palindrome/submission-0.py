class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        sl = [c.lower() for c in s if c.isalnum()]
        start, end = 0, len(sl) - 1
        while start < end:
            if sl[start] == sl[end]:
                start += 1
                end -= 1
            else:
                return False

        return True