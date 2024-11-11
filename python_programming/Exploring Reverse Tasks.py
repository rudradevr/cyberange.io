import random
import string
import base64


sep = '-' * 30


def level1():
    print(sep + " LEVEL 1 " + sep)

    # Generate a random FLAG (16 lowercase characters)
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(16)])
    ANSWER = base64.b64encode(FLAG.encode()).decode()

    print("\nBase64 representation of a random FLAG = %s" % ANSWER)
    guess = input("Enter the original FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 1!")
        return FLAG  # Return the FLAG if the guess is correct
    else:
        print("\n[x] Incorrect FLAG. Try again!")
        return None  # Return None if the guess is incorrect


def level2(FLAG):
    print(sep + " LEVEL 2 " + sep)

    # Base64 encode the FLAG for comparison
    ANSWER = base64.b64encode(FLAG.encode()).decode()

    # Ask the user for the Base64 representation of the FLAG
    guess = input("\nGive me the Base64 representation of '%s': " % FLAG).strip()

    if guess == ANSWER:
        print("\n[+] Congratulations!!\n You passed level 2!")
    else:
        print("\n[x] Incorrect Base64. Try again!")


if __name__ == '__main__':
    try:
        FLAG = None
        while FLAG is None:  # Keep running level1 until correct FLAG is provided
            FLAG = level1()
        
        level2(FLAG)  # Pass the FLAG from level1 to level2
        
    except:
        print("\n[x] Oops! Try Again!")
        exit()

    # Print the final FLAG after both levels are passed
    print("\n[+] Submit the FLAG => {}".format(FLAG))
