class Solution:
    def alienOrder(self, words: List[str]) -> str:
        child = collections.defaultdict(set)
        parent = collections.defaultdict(int)
        chars = set()
        for w1,w2 in zip(words[:-1], words[1:]):
            if len(w1)>len(w2) and w1[:len(w2)] == w2:   ##invalid case['abc', 'ab']
                return ''
            for c1, c2 in zip(w1,w2):
                if c1 != c2:
                    if c1 in child[c2]:  #invalid case['x', 'z', 'x']
                        return ''
                    if c2 not in child[c1]:
                        child[c1].add(c2)
                        parent[c2] += 1
                    break
        q = collections.deque()
        for w in words:
            for c in w:
                chars.add(c)
        for char in chars:
            if parent[char] == 0:
                del parent[char]
                q.append(char)

        res = ''
        while q:
            char = q.popleft()
            res += char
            for ch in child[char]:
                parent[ch] -= 1
                if parent[ch] == 0:
                    q.append(ch)
                    del parent[ch]
        
        return res if len(res) == len(chars) else ''