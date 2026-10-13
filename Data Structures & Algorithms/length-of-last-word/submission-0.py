class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(" ")
        words.reverse()

        for w in words:
            if w: return len(w)
