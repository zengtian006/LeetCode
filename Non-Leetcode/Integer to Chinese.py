lessThan10 = ['零', '一', '贰', '叁', '肆', '伍', '六', '七', '八' ,'九']
lessThan1000 = ['','拾','佰','千']
thousands = ["", "万", "亿", "兆"]
def numberToWords(num: int) -> str:
    
    if num == 0 :
        return "零"
    res = ''
    i = 0
    while num>0:
        if num%10000 != 0:
            res = helper(num%10000) + thousands[i] + res
        num //= 10000
        i += 1
    print(res)
    return res.strip()

def helper(num):
    res = []
    i = 0
    while num > 0:
      if num % 10 != 0:
        res.append(lessThan10[num%10]+lessThan1000[i])
      else:
        if i != 0 and res[-1] != "零": 
          res.append('零')
      num //=10
      i+=1
    return "".join(res[::-1])

numberToWords(10051002)