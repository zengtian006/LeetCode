# Trie


Trie 为字典树或前缀树，如下图，根结点不存储数据，子节点，存储字符，从root到end结点组成一个单词，这种结构用于单词的前缀查找

```
        root
        /  \
       C    D
      /      \
     A        O
    / \        \
   T   R         G
(end) (end)     (end) 
```


```python
class TrieNode:
    def __init__(self):
        self.child = collections.defaultdict(TrieNode)
        self.isWord = False
        self.word = ''

class Trie:
    def __init__(self):
        root = TrieNode()
    
    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.child[w]
        cur.isWord = True # end结点 
        cur.word = word

    def search(self, word): #完整次查找
        cur = self.root
        for w in word:
            if w in cur.child:
                cur = cur.child[w]
            else:
                return False
        return True

    def searchWith(self, prefix): #前缀查找
        cur = self.root
        for p in prefix:
            if p in cur.child:
                cur = cur.child[p]
            else:
                return False
        res = []
        stack = []
        stack.append(cur)
        while stack:
            node = stack.pop()
            if node.isWord:
                res.append(node.word)
            for ch in node.child:
                stack.append(node.child[ch])
        return res


```


- 练习题
[Leetcode 208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)
[Leetcode 211. Add and Search Word - Data structure design](https://leetcode.com/problems/add-and-search-word-data-structure-design/description/)
[Leetcode 642. Design Search Autocomplete System](https://leetcode.com/problems/design-search-autocomplete-system/)