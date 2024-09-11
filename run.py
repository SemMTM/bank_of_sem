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
ALL_USERNAMES = SHEET.worksheet("user-details").col_values(1)
ALL_PASSWORDS = SHEET.worksheet("user-details").col_values(2)


def user_log_in():
    """
    Ask user to log in
    """
    print("***********************")
    print("Welcome to Bank of Sem")

    while True:
        print("***********************\n")
        print("1. Log In")
        print("2. Create An Account\n")
        print("***********************")    
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

    new_user_details = [new_username, new_password]

    print("Adding new user details to database...\n")
    user_worksheet = SHEET.worksheet("user-details")
    user_worksheet.append_row(new_user_details)
    print("Your new account has been created\n")


def validate_new_username(username):
    """
    Validate the user entered username against the database.
    Raises an error if the Username is not unique.
    """
    existing_username = any(x == username for x in ALL_USERNAMES)

    if existing_username == True:
        print("Username already exists. Please enter a new username\n")
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
    print("***********************\n")
    print("Please enter your log in details")
    existing_username = input("Please enter your username:\n")
    existing_password = input("Please enter your password:\n")
    print("***********************")  
    
    if validate_existing_login_details(existing_username, int(existing_password)):
        d


def get_existing_login_details():
    existing_credentials = {ALL_USERNAMES: password for ALL_USERNAMES, password in zip(ALL_USERNAMES, ALL_PASSWORDS)}

    return existing_credentials


def validate_existing_login_details(username, password):
    existing_credentials = get_existing_login_details()


def main():
    """
    Run all program functions.
    """
    user_log_in()


main()