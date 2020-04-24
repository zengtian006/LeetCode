class TrieNode:
    
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False
        
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.isWord = True
        

    def search(self, word: str) -> bool:
        if not word: 
            return False
        cur = self.root
        stack = []
        stack.append((cur, 0))
        while stack:
            cur, idx = stack.pop()
            if idx == len(word):
                if cur.isWord:
                    return True
            else:
                if word[idx] == '.':
                    for ch in cur.child:
                        stack.append((cur.child[ch], idx+1))
                elif word[idx] in cur.child:
                    stack.append((cur.child[word[idx]], idx+1))

        return False