import random
import string
import json

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
    formatted_flag = "flag{Decimal_my_friend_" + ''.join([hex(ord(x))[2:] for x in FLAG]) + "}"

    print("\nDecimal representation of the characters of the FLAG = %s" % ANSWER)
    guess = input("Enter the FLAG (format: flag{Decimal_my_friend_hexcode}): ").strip()

    if guess == formatted_flag:
        print("\n[+] Congratulations!!\n You passed level 2!")
        return formatted_flag  # Return the formatted flag to make it accessible in the main block.
    else:
        raise


if __name__ == '__main__':
    try:
        level1()
        formatted_flag = level2()  # Capture the formatted flag from level 2
    except:
        print("\n[x] Oops! Try Again!")
        exit()

    print("\n[+] Submit the FLAG => %s" % formatted_flag)
