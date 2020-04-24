class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False
        
class Trie:

    def __init__(self):
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        cur =self.root
        for w in word:
            cur = cur.child[w]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        cur = self.root
        for w in word:
            if w in cur.child:
                cur = cur.child[w]
            else:
                return False
        return cur.isWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for w in prefix:
            if w in cur.child:
                cur = cur.child[w]
            else:
                return False
        return True