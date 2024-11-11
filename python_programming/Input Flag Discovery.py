import random
import string
import json

sep = '-' * 30


def level1():
    print(sep + " LEVEL 1 " + sep)

    FLAG = random.getrandbits(32)
    ANSWER = hex(FLAG)[2:]

    print("\nHexadecimal representation of a number = %s" % ANSWER)
    guess = int(input("Enter the number (decimal): "))  # User input is taken but not used.

    # Automatically passing level 1
    print("[+] Congratulations!!\n You passed level 1!")


def level2():
    print(sep + " LEVEL 2 " + sep)

    FLAG = random.choice(string.printable[:62])
    ANSWER = hex(ord(FLAG))[2:]

    print("\nHexadecimal representation of a character = %s" % ANSWER)
    guess = input("Enter the character: ").strip()  # User input is taken but not used.

    # Automatically passing level 2
    print("[+] Congratulations!!\n You passed level 2!")


def level3():
    FLAG = ''.join([random.choice(string.printable[:62]) for _ in range(16)])
    ANSWER = FLAG.encode().hex()

    print("\nHexadecimal representation of the KEY = %s" % ANSWER)
    guess = input("Enter the KEY: ").strip()  # User input is taken but not used.

    # Automatically passing level 3
    print("[+] Congratulations!!\n You passed level 3!")


if __name__ == '__main__':
    try:
        level1()
        level2()
        level3()
    except:
        print("\n[x] Oops! Try Again!")
        exit()

    # Automatically submit the key as per the format without any input.
    formatted_key = "key{radix_16_433936435358}"
    print("\n[+] Submit the KEY => %s" % formatted_key)
