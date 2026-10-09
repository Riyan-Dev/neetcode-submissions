class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalin(s):

            return s and s == s[::-1]

        def dfs(pals, st):

            if not st:
                res.append(pals.copy())
                return
            
            if isPalin(st):
                res.append(pals + [st])

            for i in range(1, len(st)):

                right = st[i:]
                left = st[:i]
                if isPalin(left):
                    pals.append(left)
                    dfs(pals, right)
                    pals.pop()
                
        
        dfs([], s)
        return res
                


            
         

    