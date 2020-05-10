class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        count, cur_words = 0, []
        res = []
        for word in words:
            if count+ len(word) + len(cur_words) > maxWidth:
                spaces = maxWidth - count
                if len(cur_words) == 1:
                    cur_words[0] += ' '*spaces
                else:  
                    for i in range(spaces):
                        cur_words[i % (len(cur_words)-1)] += ' '
                res.append("".join(cur_words))
                count, cur_words = 0, []
            count+=len(word)
            cur_words.append(word)
        
        #last row
        spaces = maxWidth - count - (len(cur_words)-1)
        res.append(" ".join(cur_words)+" "*spaces)
        return res