class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = set()
        for i, a in enumerate(words):
            for j, b in enumerate(words):
                if i == j: continue
                if len(a) > len(b): continue
                if a in b: ans.add(a)

        return list(ans)