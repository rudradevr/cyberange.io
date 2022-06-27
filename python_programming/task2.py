import random
import string

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)
    
    FLAG = random.choice(string.printable[:62])
    ANSWER = ord(FLAG)

    print("\nDecimal representation of a character = %s" % ANSWER)
    guess = input("Enter the character: ").strip()

    if guess == FLAG:
        print("[+] Congratulations!!\n You passed level 1!")
    else:
        raise


def level2():
    print(sep + " LEVEL 2 " + sep)

    FLAG = ''.join([random.choice(string.printable[:62]) for _ in range(6)])
    ANSWER = ' '.join([str(ord(x)) for x in FLAG])

    print("\nDecimal representation of the characters of the FLAG = %s" % ANSWER)
    guess = input("Enter the FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 2!")
    else:
        raise


if __name__ == '__main__':
    FLAG = "flag{Decimal_my_friend!}"

    try:
        level1()
        level2()
    except:
        exit("\n[x] Oops! Try Again!")

    print("\n[+] Submit the FLAG => %s" % FLAG)
