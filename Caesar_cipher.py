import string

alpha = {i:j for j,i in enumerate(string.ascii_lowercase)}
digi = {int(j):i for j,i in enumerate(string.ascii_lowercase)}

def decode(text:str,shift:int):
    text = text.lower()
    if shift>25:
        shift = shift%25
    ans = ''
    for i in text:
        if i not in string.ascii_lowercase:
            ans += i
            continue
        num = int(alpha[i])
        if num<shift:
            num = 25+num-shift
        else:
            num = num-shift
        ans = ans+digi[num]
    return ans

def encode(text:str,shift:int):
    text = text.lower()
    if shift>25:
        shift = shift%25
    ans =''
    for i in text:
        if i not in string.ascii_lowercase:
            ans += i
            continue
        num = int(alpha[i])
        if num+shift>25:
            num = num+shift-25
        else:
            num = num + shift
        ans = ans+digi[num]
    return ans


