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
    print("Welcome to Bank of Sem.")

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
            print("Log in successful!\n") 
            break
        else: 
            print("Please select a valid option.\n")

            
user_log_in()
