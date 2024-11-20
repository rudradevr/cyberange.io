import random
import string
import base64

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)

    # Generate a random 20-character lowercase string as the FLAG
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(20)])
    # Encode the FLAG in Base32
    ANSWER = base64.b32encode(FLAG.encode()).decode()

    # Prompt the user to guess the original FLAG based on the Base32 representation
    print("\nBase32 representation of a random FLAG = %s" % ANSWER)
    guess = input("Enter the original FLAG: ").strip()

    # Check if the user's guess matches the original FLAG
    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 1!")
    else:
        print("\n[x] Incorrect. Try again.")
        raise ValueError("Level 1 failed")

def level2():
    print(sep + " LEVEL 2 " + sep)
    
    # Generate another random 20-character lowercase string as the FLAG
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(20)])
    # Encode this FLAG in Base32
    ANSWER = base64.b32encode(FLAG.encode()).decode()

    # Prompt the user to provide the Base32 representation for the given FLAG
    guess = input("\nGive me the Base32 representation of '%s': " % FLAG).strip()

    # Check if the user's answer matches the encoded Base32 answer
    if guess == ANSWER:
        print("\n[+] Congratulations!!\n You passed level 2!")
    else:
        print("\n[x] Incorrect. Try again.")
        raise ValueError("Level 2 failed")

if __name__ == '__main__':
    try:
        # Run level 1
        level1()
        # Run level 2
        level2()
    except Exception as e:
        print("\n[x] Oops! Try Again!")
        exit()

    # Show the final FLAG after successfully completing both levels
    print("\n[+] You completed both levels!")
