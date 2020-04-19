# BFS
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        dic = set(wordList)
        if endWord not in dic:
            return 0
        q = collections.deque()
        q.append(beginWord)
        steps = 0
        while q:
            size = len(q)
            steps += 1
            for _ in range(size):
                word = q.popleft()
                for i in range(len(word)):
                    for k in range(ord('a'), ord('z')+1):
                        w = word[:i]+chr(k) +word[i+1:]
                        if w in dic:
                            if w == endWord:
                                return steps+1
                            else:
                                q.append(w)
                                dic.remove(w)
        return 0