import random
import string
import base64

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)

    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(16)])
    ANSWER = base64.b85encode(FLAG.encode()).decode()

    print("\nBase85 representation of a random FLAG = %s" % ANSWER)
    guess = input("Enter the original FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 1!")
    else:
        raise


def level2():
    print(sep + " LEVEL 2 " + sep)
    
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(16)])
    ANSWER = base64.b85encode(FLAG.encode()).decode()

    guess = input(
        "\nGive me the Base85 representation of '%s': " % FLAG).strip()

    if guess == ANSWER:
        print("\n[+] Congratulations!!\n You passed level 2!")
    else:
        raise


if __name__ == '__main__':
    FLAG = "flag{Paul_E_Rutter}"

    try:
        level1()
        level2()
    except:
        exit("\n[x] Oops! Try Again!")

    print("\n[+] Submit the FLAG => %s" % FLAG)
