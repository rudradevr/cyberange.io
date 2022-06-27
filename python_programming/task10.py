import random

FLAG = "flag{Winner_Winner!!!}"
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
        for _ in range(lim):
            num = random.getrandbits(64)
            radix = random.randint(2, 9)
            c = to_base(num, radix)

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
        exit(sep + "[x] Oops! Try Again!" + str(e))
