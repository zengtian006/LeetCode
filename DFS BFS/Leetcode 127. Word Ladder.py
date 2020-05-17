# BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = set(wordList)
        if endWord not in dic:
            return 0
        
        step = 1
        q = collections.deque()
        q.append(beginWord)
        while q:
            size = len(q)
            for _ in range(size):
                word = q.popleft()
                for i in range(len(word)):
                    for char in range(ord('a'), ord('z')+1):
                        char = chr(char)
                        new_word = word[:i] +char +word[i+1:]
                        if new_word == endWord:
                            return step+1
                        if new_word in dic:
                            q.append(new_word)
                            dic.remove(new_word)
            step+=1
        return 0