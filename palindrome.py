while True:
    try:
        n = int(input("enter an integer:   "))
    except:
        print("Enter an integer")
        continue

    if (len(str(n)) > 1) and (n > 0):
        if str(n) == str(n)[::-1]:
            print("its a palindrome!")
        else:
            print("not a palindrome")

    else:
        print("Pls enter a valid input")

# exp
# checks first if its a integer or not
# then checks if its a valid integer
# then reverses the integer if its same as the original then its a palindrome