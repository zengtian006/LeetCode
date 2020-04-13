class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res=''
        for strr in strs:
            res += str(len(strr))+'$'+strr
        print(res)
        return res

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        i = 0
        while i<len(s):
            p = s.find('$', i)
            length = int(s[i:p])
            res.append(s[p+1:p+1+length])
            i = p+1+length
        return res