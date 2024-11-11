import random
import string
import base91  
#pip install base91

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)

    # Generate a random 16-character FLAG
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(16)])
    # Encode the FLAG in Base91
    ANSWER = base91.encode(FLAG.encode())

    print("\nBase91 representation of a random FLAG = %s" % ANSWER)
    guess = input("Enter the original FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 1!")
    else:
        print("[x] Incorrect. Try again.")

def level2():
    print(sep + " LEVEL 2 " + sep)

    # Generate a random 16-character FLAG
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(16)])
    # Encode the FLAG in Base91
    ANSWER = base91.encode(FLAG.encode())

    guess = input(
        "\nGive me the Base91 representation of '%s': " % FLAG).strip()

    if guess == ANSWER:
        print("\n[+] Congratulations!!\n You passed level 2!")
    else:
        print("[x] Incorrect. Try again.")

if __name__ == '__main__':
    try:
        level1()
        level2()
    except Exception as e:
        print(f"\n[x] Oops! {e} Try Again!")
        exit()

    print("\n[+] Submit the FLAG => {}".format(FLAG))
