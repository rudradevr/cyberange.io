import random
import string
import base58  # pip install base58

sep = '-' * 30

def level1():
    print(sep + " LEVEL 1 " + sep)

    # Generate a random FLAG
    FLAG = ''.join([random.choice(string.ascii_lowercase) for _ in range(20)])

    # Base58 encode the FLAG
    ANSWER = base58.b58encode(FLAG.encode()).decode()

    # Display the Base58 representation and ask for the original FLAG
    print("\nBase58 representation of a random FLAG = %s" % ANSWER)
    guess = input("Enter the original FLAG: ").strip()

    if guess == FLAG:
        print("\n[+] Congratulations!!\n You passed level 1!")
        return FLAG  # Return the FLAG after successful completion
    else:
        print("\n[x] Incorrect FLAG. Try again!")
        return None  # Return None if the answer is incorrect

def level2(FLAG):
    print(sep + " LEVEL 2 " + sep)
    
    # Base58 encode the FLAG
    ANSWER = base58.b58encode(FLAG.encode()).decode()

    # Display the original FLAG and ask for the Base58 representation
    guess = input("\nGive me the Base58 representation of '%s': " % FLAG).strip()

    if guess == ANSWER:
        print("\n[+] Congratulations!!\n You passed level 2!")
    else:
        print("\n[x] Incorrect Base58. Try again!")

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
