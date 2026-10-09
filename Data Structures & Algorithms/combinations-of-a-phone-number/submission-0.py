class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        strs = [digMap[d] for d in digits]

        def dfs(sub, i):
            if i >= len(digits):
                res.append("".join(sub))
                return

            for j in range(len(strs[i])):
                sub.append(str(strs[i][j]))
                dfs(sub, i+1)
                sub.pop()

        dfs([], 0)
        return res
