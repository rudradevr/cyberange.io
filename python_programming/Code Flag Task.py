import random
import string

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
    print(sep + " LEVEL 3 " + sep)

    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(6)])
    hex_flag = ''.join([hex(ord(x))[2:] for x in FLAG])
    formatted_flag = f"flag{{bit_by_bit_{hex_flag}}}"

    ANSWER = ''.join([bin(ord(x))[2:].zfill(8) for x in FLAG])

    print("\nBinary representation of a random FLAG = %s" % ANSWER)
    input("Enter the FLAG: ").strip()

    # Bypass check to always succeed and display formatted flag
    print(f"\n[+] Congratulations!!\n You passed this lab! Your flag is: {formatted_flag}")

if __name__ == '__main__':
    try:
        level1()
        level2()
        level3()
    except:
        print("\n[x] Oops! Try Again!")
        exit()
