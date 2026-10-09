class WordDictionary:

    def __init__(self):
        self.tree = {}

    def addWord(self, word: str) -> None:
        curNode = self.tree
        for a in word:
            if a in curNode:
               curNode = curNode[a]
               continue
            else:
                curNode[a] = {} 
                curNode = curNode[a]
        curNode['end'] = 1


    def search(self, word: str) -> bool:
        
        def dfs(tree, i):
            if i >= len(word):
                return True if tree and 'end' in tree else False
            
            if word[i] in tree:
                return dfs(tree[word[i]], i+1)
            elif word[i] == ".":
                for subTree in tree:
                    if subTree == 'end': continue
                    if dfs(tree[subTree], i+1):
                        return True
                    else:
                        continue      
                return False
            else:
                return False

        return dfs(self.tree, 0)