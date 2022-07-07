import random
import json


FLAG = json.load(open('flags.json'))["flag10"]
alpha = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
sep = '\n' + '-'*50 + '\n'


def to_base(num, radix):
    res = ""
    while num:
        res += alpha[num % radix]
        num//= radix
    return res[::-1] or "0"


if __name__ == '__main__':
    lim = 10
    score = 0

    try:
        for level in range(1, lim+1):
            num = random.getrandbits(64)
            radix = random.randint(2, 9)
            c = to_base(num, radix)

            print("\n[ ===== LEVEL: {} Score: {} ===== ]".format(level, score))
            print("\n[=] Conver this Base{} number into Decimal: {}".format(radix, c))
            guess = int(input('[?]> ').strip())

            if guess == num:
                print("[+] Well done!!!")
                score += 1
            else:
                print("[-] Nope!!!")
        
        if score == lim:
            print(sep)
            print("[+] Congratulations!!")
            print("[+] Submit the FLAG => %s" % FLAG)
        else:
            raise Exception("( Score = {}/{} )".format(score, lim))

    except Exception as e:        
        print(sep + "[x] Oops! Try Again!\n" + str(e))
        exit()
