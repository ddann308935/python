# Name: Daniel
# Date: 04/09/2024
# Purpose: Defining functions for each component (1-3)

# Component 1 – Registration (creating a new user account)
def new_acc(new_user, new_pass) -> str:

    # Check password length
    while len(new_pass) < 8 :
        new_pass = input("Password needs to be minimum 8 characters long.\nPlease create a password: ")
        print()

    # Open the text file and append the new username and password
    account = open("basicLogin_Reg/accounts.txt", "a")
    account.write(f"{new_user},{new_pass}\n")
    account.close()

    print(f"Username: '{new_user}' is now registered.\n")

# Component 2 – Log In (checking username and password)
def check_acc(check_user, check_pass) -> int:

    # Open the text file and read all lines
    account = open("basicLogin_Reg/accounts.txt", 'r')
    allaccounts = account.readlines() # each line is an element within a list 

    # Loop through all elements
    for n in allaccounts:
        n = n.strip()
        a, b = n.split(",") 
        
        # if statements to compare the prompted account with the existing accounts
        if check_user == a and check_pass == b:
            print("Verifed account.\n")
            account.close()
            return 0
        elif check_user == a or check_pass == b:
            print("Incorrect username or password.\n")
            account.close()
            return 1
        else:
            continue
    # If there are no matches to all exisiting accounts, then the account is unverified
    print("Unverified account. Please register.\n")
    account.close()
    return 2

# Component 3 – View Existing Accounts (only with successful login)
def view_acc():
    # open the text file and read all lines into a list
    f = open("basicLogin_Reg/accounts.txt", "r") 
    allaccounts = f.readlines()

    # loop through all lines (accounts)
    i = 1
    for n in allaccounts:
        n = n.strip()
        c, d = n.split(",")
        
        # print the ranked number and username
        print(f"{i}: {c}")
        i += 1
    print()
    f.close()