class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(sub, o, c, n):
            print(sub, o, c, n)
            if len(sub) == n*2:
                res.append("".join(sub))
                return 

            if o < n:
                sub.append("(")
                dfs(sub, o+1, c, n)
                sub.pop()
            if o > c:
                sub.append(")")
                dfs(sub, o, c+1, n)
                sub.pop()


        dfs(['('], 1, 0, n)
        return res

#      (

#      ) (
#    ()     