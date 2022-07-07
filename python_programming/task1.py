import random
import string
import json


FLAG = json.load(open('flags.json'))["flag1"]
sep = '-' * 30


def level1():
    print(sep + " LEVEL 1 " + sep)

    FLAG = random.getrandbits(32)
    ANSWER = bin(FLAG)[2:]

    print("\nBinary representation of a number = %s" % ANSWER)
    guess = int(input("Enter the number (decimal): "))

    if guess == FLAG:
        print("[+] Congratulations!!\n You passed level 1!")
    else:
        raise


def level2():
    print(sep + " LEVEL 2 " + sep)

    FLAG = random.choice(string.ascii_lowercase)
    ANSWER = bin(ord(FLAG))[2:]

    print("\nBinary representation of a character = %s" % ANSWER)
    guess = input("Enter the character: ").strip()

    if guess == FLAG:
        print("[+] Congratulations!!\n You passed level 2!")
    else:
        raise


def level3():
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(6)])
    ANSWER = ''.join([bin(ord(x))[2:].zfill(8) for x in FLAG])

    print("\nBinary representation of a random FLAG = %s" % ANSWER)
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

    print("\n[+] Submit the FLAG => {}".format(FLAG))
