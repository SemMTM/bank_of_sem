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
            print("Log in successful!\n") 
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

    print(new_username)

    while True:
        print("Your password must be a 4 digit number")
        new_password = input("Please enter a password: \n")
        print("***********************\n")

        if validate_new_password(new_password):
            break

    print(new_password)


def validate_new_username(username):
    """
    Validate the user entered username against the database.
    Raises an error if the Username is not unique.
    """
    all_usernames = SHEET.worksheet("user-details").col_values(1)
    existing_username = any(x == username for x in all_usernames)

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

def main():
    user_log_in()

main()