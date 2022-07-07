import random
import string
import json


FLAG = json.load(open('flags.json'))["flag3"]
sep = '-' * 30


def level1():
    print(sep + " LEVEL 1 " + sep)

    FLAG = random.getrandbits(32)
    ANSWER = hex(FLAG)[2:]

    print("\nHexadecimal representation of a number = %s" % ANSWER)
    guess = int(input("Enter the number (decimal): "))

    if guess == FLAG:
        print("[+] Congratulations!!\n You passed level 1!")
    else:
        raise


def level2():
    print(sep + " LEVEL 2 " + sep)

    FLAG = random.choice(string.printable[:62])
    ANSWER = hex(ord(FLAG))[2:]

    print("\nHexadecimal representation of a character = %s" % ANSWER)
    guess = input("Enter the character: ").strip()

    if guess == FLAG:
        print("[+] Congratulations!!\n You passed level 2!")
    else:
        raise


def level3():
    FLAG = ''.join([random.choice(string.printable[:62]) for _ in range(16)])
    ANSWER = FLAG.encode().hex()

    print("\nHexadecimal representation of the FLAG = %s" % ANSWER)
    guess = input("Enter the FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 3!")
    else:
        raise


if __name__ == '__main__':
    try:
        level1()
        level2()
        level3()
    except:
        print("\n[x] Oops! Try Again!")
        exit()

    print("\n[+] Submit the FLAG => %s" % FLAG)
