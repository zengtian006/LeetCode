class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = cows = 0
        dic = {}
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                bulls += 1
            else:
                dic[secret[i]] = dic.get(secret[i], 0)+1

        for i in range(len(guess)):
            if guess[i] != secret[i] and dic.get(guess[i], 0) != 0:
                cows += 1
                dic[guess[i]] -= 1
        return str(bulls)+"A"+str(cows)+"B"


        # 第一轮遍历后，bulls统计完，把剩余没比较的secret放入dic，再统计cows。避免这个case s='1100'  g = '0011'  0A4B