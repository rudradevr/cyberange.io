import random
import string
import base91 # pip install base91

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)

    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(16)])
    ANSWER = base91.encode(FLAG.encode())

    print("\nBase91 representation of a random FLAG = %s" % ANSWER)
    guess = input("Enter the original FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 1!")
    else:
        raise


def level2():
    print(sep + " LEVEL 2 " + sep)

    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(16)])
    ANSWER = base91.encode(FLAG.encode())

    guess = input(
        "\nGive me the Base91 representation of '%s': " % FLAG).strip()

    if guess == ANSWER:
        print("\n[+] Congratulations!!\n You passed level 2!")
    else:
        raise


if __name__ == '__main__':
    FLAG = "flag{from_0x21_to_0x7E}"

    try:
        level1()
        level2()
    except:
        exit("\n[x] Oops! Try Again!")

    print("\n[+] Submit the FLAG => %s" % FLAG)
