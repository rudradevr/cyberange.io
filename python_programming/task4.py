import random
import string

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)

    FLAG = random.getrandbits(32)
    ANSWER = oct(FLAG)[2:]

    print("\nOctal representation of a number = %s" % ANSWER)
    guess = int(input("Enter the number (decimal): "))

    if guess == FLAG:
        print("[+] Congratulations!!\n You passed level 1!")
    else:
        raise


def level2():
    print(sep + " LEVEL 2 " + sep)
    
    FLAG = random.choice(string.printable[:62])
    ANSWER = oct(ord(FLAG))[2:]

    print("\nOctal representation of a character = %s" % ANSWER)
    guess = input("Enter the character: ").strip()

    if guess == FLAG:
        print("[+] Congratulations!!\n You passed level 2!")
    else:
        raise


def level3():
    FLAG = ''.join([random.choice(string.printable[:62]) for _ in range(8)])
    ANSWER = ' '.join([oct(ord(x))[2:] for x in FLAG])

    print("\nBinary representation of the FLAG = %s" % ANSWER)
    guess = input("Enter the FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 3!")
    else:
        raise


if __name__ == '__main__':
    FLAG = "flag{Octal_uses_0_to_7}"

    try:
        level1()
        level2()
        level3()
    except:
        exit("\n[x] Oops! Try Again!")

    print("\n[+] Submit the FLAG => %s" % FLAG)
