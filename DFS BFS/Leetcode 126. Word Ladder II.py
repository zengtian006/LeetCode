# BFS
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        dic = set(wordList)
        if endWord not in dic:
            return []
        res = []
        q = collections.deque()
        q.append((beginWord, [beginWord]))
        steps = 0
        min_steps = float('inf')
        while q:
            size = len(q)
            remove = set()
            steps += 1
            if steps > min_steps:
                break
            for _ in range(size):
                word, seq = q.popleft()
                for i in range(len(word)):
                    for k in range(ord('a'), ord('z')+1):
                        w = word[:i]+chr(k)+word[i+1:]
                        if w in dic:
                            if w == endWord:
                                min_steps=steps=1
                                res.append(seq+[endWord])
                            else:
                                remove.add(w)
                                q.append((w, seq+[w]))
            for w in remove:
                dic.remove(w)
        return res