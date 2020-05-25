class Solution:
    adds = {'one':1, 'two':2, 'three':3, "four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10,"eleven":11,"twelve":12,"thirteen":13,"fourteen":14, "fifteen":15,"sixteen":16,"seventeen":17,"eighteen":18,"nineteen":19,"twenty":20,"thirty":30,"forty":40,"fifty":50,"sixty":60,"seventy":70,"eighty":80,"ninety":900}
    muls = {'hundred':100, 'thousand':1000, 'million':1000000, 'billion':1000000000}

    def EnglishToInt(self, strr: string) -> int:
        strr = 'One Hundred Twenty Three'
        strr = 'Three hundred million'
        strr = 'Five Hundred Thousand'
        tokens = strr.split()
        print(self.helper(tokens))
        return self.helper(tokens)
        
    def helper(self, tokens):
        sums = 0
        for i, token in enumerate(tokens):
            token = token.lower()
            if token in self.adds:
                sums += self.adds[token]
            else:
                while i<len(tokens) and tokens[i].lower() in self.muls:
                    sums *= self.muls[tokens[i].lower()]
                    i+=1
                return sums+(self.helper(tokens[i:]) if i<len(tokens) else 0)
        return sums
