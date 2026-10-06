class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = []

        for s in strs:
            encoded_str.append(str(len(s)))
            encoded_str.append('#')
            encoded_str.append(s)

        
        return ''.join(encoded_str)         

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            print(s[i:j])
            lenght = int(s[i:j])
            i = j + 1
            j = i + lenght
            res.append(s[i:j])
            i = j

        return res



        

