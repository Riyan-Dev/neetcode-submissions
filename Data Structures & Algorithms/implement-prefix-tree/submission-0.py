class PrefixTree:

    def __init__(self):
        self.tree = {}

    def insert(self, word: str) -> None:
        currNode = self.tree
        for alp in word:
            if alp in currNode:
                currNode = currNode[alp]
                continue
            else:
                currNode[alp] = {}
                currNode = currNode[alp]
        
        currNode['end'] = 1

    def search(self, word: str) -> bool:
        currNode = self.tree
        for alp in word:
            if alp in currNode:
                currNode = currNode[alp]
                continue
            else: 
                return False
        
        return True if 'end' in currNode else False
        
    def startsWith(self, prefix: str) -> bool:
        currNode = self.tree
        for alp in prefix:
            if alp in currNode:
                currNode = currNode[alp]
                continue
            else: 
                return False

        return True
        