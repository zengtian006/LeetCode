class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False
        self.word = ""
        self.times = 0
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, sentence, times):
        cur = self.root
        for char in sentence:
            cur = cur.child[char]
        if not cur.isWord:
            cur.isWord = True
            cur.word = sentence
            cur.times = times if times else 1
        else:
            cur.times += 1
        
    def search(self, char):
        res = []
        dic = {}
        cur = self.root
        for c in char:
            if c not in cur.child:
                return None
            cur = cur.child[c]
            
        stack = []
        stack.append(cur)
        while stack:
            node = stack.pop()
            if node.isWord:
                dic[node.word] = node.times
            for ch in node.child:
                n = node.child[ch]
                stack.append(n)
        i = 3
        for k,v in sorted(dic.items(), key=lambda x:(-x[1],x[0]) ):
            if i ==0:
                break
            res.append(k)
            i-=1
        return res
        
        
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.inp = ""
        self.trie = Trie()
        for sentence,time in zip(sentences,times):
            self.trie.insert(sentence, time)

    def input(self, c: str) -> List[str]:
        if c == "#":
            self.trie.insert(self.inp, None)
            self.inp = ""
            return []
        self.inp+=c
        return self.trie.search(self.inp)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)