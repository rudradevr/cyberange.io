import random
import string

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)

    # Generate a random 32-bit number and convert it to octal
    KEY = random.getrandbits(32)
    ANSWER = oct(KEY)[2:]

    print("\nOctal representation of a number = %s" % ANSWER)
    guess = int(input("Enter the number (decimal): "))

    if guess == KEY:
        print("[+] Congratulations!!\n You passed level 1!")
        return KEY  # Return KEY for use in final key generation
    else:
        print("[x] Incorrect. Try again.")
        return None

def level2():
    print(sep + " LEVEL 2 " + sep)
    
    # Randomly select a printable character and convert it to octal
    KEY = random.choice(string.printable[:62])
    ANSWER = oct(ord(KEY))[2:]

    print("\nOctal representation of a character = %s" % ANSWER)
    guess = input("Enter the character: ").strip()

    if guess == KEY:
        print("[+] Congratulations!!\n You passed level 2!")
        return KEY  # Return KEY for use in final key generation
    else:
        print("[x] Incorrect. Try again.")
        return None

if __name__ == '__main__':
    try:
        # Run each level until the user passes it
        KEY1 = None
        while KEY1 is None:
            KEY1 = level1()
        
        KEY2 = None
        while KEY2 is None:
            KEY2 = level2()
    except Exception as e:
        print("\n[x] Oops! Try Again!")
        exit()

    # Generate the final key using the results from level 1 and level 2
    final_key = "custom{" + oct(KEY1)[2:] + '_' + oct(ord(KEY2))[2:] + "}"
    print("\n[+] Submit the KEY => {}".format(final_key))
