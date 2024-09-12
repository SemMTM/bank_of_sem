import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('bank_of_sem')
USER_DETAILS_SHEET = SHEET.worksheet("user-details")
ALL_USERNAMES = SHEET.worksheet("user-details").col_values(1)
ALL_PASSWORDS = SHEET.worksheet("user-details").col_values(2)
ALL_BALANCES = SHEET.worksheet("user-details").col_values(3)


def user_log_in():
    """
    Ask user to log in
    """
    print("***********************")
    print("Welcome to Bank of Sem\n")

    while True:
        print("***********************")
        print("1. Log In")
        print("2. Create An Account")
        print("***********************\n")    
        option = input("Please select an option (1-2):\n")
        if option == '1':
            existing_user_log_in() 
            break
        elif option == '2':
            create_account() 
            break
        else: 
            print("Please select a valid option\n")


def create_account():
    """
    Create a new username and upload data to spreadsheet
    """
    while True:
        print("***********************\n")
        print("Your new username must be unique")
        new_username = input("Please enter a username:\n")
        
        if validate_new_username(new_username):
            break

    while True:
        print("Your password must be a 4 digit number")
        new_password = input("Please enter a password: \n")
        print("***********************\n")

        if validate_new_password(new_password):
            break

    new_user_details = [new_username, new_password, 0]

    print("Adding new user details to database...\n")
    user_worksheet = SHEET.worksheet("user-details")
    user_worksheet.append_row(new_user_details)
    print("Your new account has been created\n")
    print("Please restart the program and login.")


def validate_new_username(username):
    """
    Validate the user entered username against the database.
    Raises an error if the Username is not unique.
    """
    existing_username = any(x == username for x in ALL_USERNAMES)

    if existing_username == True:
        print("\nUsername already exists. Please enter a new username\n")
        create_account()
    else:
        print("New username created\n")
        return True


def validate_new_password(password):
    """
    Validates users password. Checks if it is 4 numbers.
    """
    try:
        int(password)
        if len(password) != 4:
            print(f"Invalid password. Password must be 4 numbers, you entered {len(password)}, please try again. \n")
            return False
    except ValueError:
        print("Invalid password. Password must be 4 numbers, please try again. \n")
        return False

    return True


def existing_user_log_in():
    """
    Checks for existing user credentials in the database and allows user to log in. 
    """
    print("\n***********************")
    print("Please enter your log in details\n")
    existing_username = input("Enter your username:\n")
    existing_password = input("\nEnter your password:\n")
    print("\n***********************")  
    
    if validate_existing_login_details(existing_username, existing_password):
        print("Correct Login Details\n")
        main_menu(existing_username)
    else:
        print("Incorrect Details\n")
        existing_user_log_in()


def get_existing_login_details():
    existing_credentials = {ALL_USERNAMES: password for ALL_USERNAMES, password in zip(ALL_USERNAMES, ALL_PASSWORDS)}

    return existing_credentials


def validate_existing_login_details(username, password):
    existing_credentials = get_existing_login_details()
    correct_password = existing_credentials.get(username)

    if username in existing_credentials and correct_password == password:
        return True
    else:
        return False


def main_menu(username):

    print("\n***********************")
    print("Please select an option\n")
    print("1. Show Balance")
    print("2. Withdraw/Deposit Funds")
    print("3. Send Money")
    print("4. See Account History")
    print("5. Exit")
    print("***********************\n")
    option = input("Please select an option (1-5):\n")
    
    while True:
        if option == '1':
            show_balance(username)
            break
        elif option == '2':
            withdraw_deposit_funds_menu(username)
            break
        elif option == '3':
            withdraw_funds(username)
            break
        elif option == '4':
            print("You have selected 4")
            break
        elif option == '5':
            print("You have selected 5")
            break
        else: 
            print("Please select a valid option (1-5)\n")


def show_balance(username):
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, ALL_BALANCES)}
    balance = existing_balances.get(username)

    print(f"\nYour balance is: £{balance}\n")
    print("***********************")
    print("1. Back")
    print("***********************\n")
    option = input("Please select an option:\n")
    
    while True:
        if option == '1':
            main_menu(username)
            break


def withdraw_deposit_funds_menu(username):
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, ALL_BALANCES)}
    balance = existing_balances.get(username)

    print(f"\nYour balance is: £{balance}\n")
    print("***********************")
    print("Please select an option\n")
    print("1. Deposit Funds")
    print("2. Withdraw Funds")
    print("3. Back")
    print("***********************\n")
    option = input("Please select an option (1-3):\n")

    while True:
        if option == '1':
            deposit_funds(username)
            break
        elif option == '2':
            withdraw_funds(username)
            break
        elif option == '3':
            main_menu(username)
            break
        else: 
            print("Please select a valid option (1-3)\n")

def deposit_funds(username):
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, ALL_BALANCES)}
    balance = existing_balances.get(username)
    username_cell = USER_DETAILS_SHEET.find(username)

    print("\n***********************")
    deposit_amount = input("How much would you like to deposit?\n£")
    print("\n***********************")
    new_balance = int(balance) + int(deposit_amount)
    print("Depositing funds...\n")
    USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)
    print(f"Deposit complete. Your new balance is £{new_balance}\n")
    print("***********************")
    print("1. Back")
    print("***********************\n")
    option = input("Please select an option:\n")
    
    while True:
        if option == '1':
            withdraw_deposit_funds_menu(username)
            break


def withdraw_funds(username):
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, ALL_BALANCES)}
    balance = existing_balances.get(username)
    username_cell = USER_DETAILS_SHEET.find(username)

    print("\n***********************")
    withdraw_amount = input("How much would you like to withdraw?\n£")
    print("***********************\n")
    new_balance = int(balance) - int(withdraw_amount)
    
    if int(withdraw_amount) > int(balance) or int(balance) == 0:
        print("Insufficient funds for withdrawal, please enter a lower amount\n")
        print("***********************")
        print("1. Try again")
        print("2. Back")
        print("***********************")
        option = input("\nPlease select an option:\n")
    
        while True:
            if option == '1':
                withdraw_funds(username)
                break
            if option == '2':
                main_menu(username)
                break
    else:
        print("Withdrawing funds...\n")
        USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)
        print(f"Withdraw complete. Your new balance is £{new_balance}\n")
        print("***********************")
        print("1. Back")
        print("***********************\n")
        option = input("Please select an option:\n")
    
        while True:
            if option == '1':
                main_menu(username)
                break


def main():
    """
    Run all program functions.
    """
    user_log_in()


main()