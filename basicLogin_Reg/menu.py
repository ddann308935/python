# Name: Daniel
# Date: 04/09/2024
# Purpose: A menu to access three components: Registration, Login and View Accounts

# Importing defined functions from options.py
from options import new_acc, check_acc, view_acc

# Prompt user for their username and password
def prompt() -> str:
    username = input("Please enter username: ")
    password = input("Please enter password: ")
    print()
    return username, password

# PROGRAM
while True:
    # Print menu and prompt user's option
    num_option = input("Gelos Enterprises Account Login: \n1) Register\n2) Log In and View Accounts \n3) Exit \nYour option: ")  

    # Create a new account
    if num_option == '1':
        user, pas = prompt()
        new_acc(user, pas)
        # return to menu

    # Check for an existing account. If true, then view all accounts.
    elif num_option == '2':
        while True:
            user, pas = prompt()
            # check with existing accounts and returns an int
            num = check_acc(user, pas)

            # Verified Account
            if num == 0:
                # View existing accounts
                view_acc()
                break # return to menu

            # Incorrect username or password
            elif num == 1:
                break # ""

            # Unverified Account
            else:
                break # ""
        
    # Exit the program
    elif num_option == '3':
        print("Thank you for using our program. Goodbye.\n")
        break

    # Invalid entry
    else:
        print("Invalid Entry. Please try again.\n")
        # return to menu
