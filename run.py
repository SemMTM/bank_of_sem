import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime
from random import randint

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


def user_log_in():
    """
    Ask user to log in
    """
    print("***********************")
    print("Welcome to Bank Of Sem\n")

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
            print("\nPlease select a valid option\n")


def create_account():
    """
    Create a new username and upload data to spreadsheet
    """
    time_now = datetime.now()
    account_type = ''

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

    while True:
        print("Here are our available account types:")
        print("1. Current Account - A regular account with no limits")
        print("2. Growth Account - An account with a £15,000 balance limit and interest gained of 1% per log in")
        account_type_selection = input("\nPlease select an account type:\n")

        if account_type_selection == '1':
            account_type = 'Current Account'
            break
        elif account_type_selection == '2':
            account_type = 'Growth Account' 
            break
        else: 
            print("\nPlease select a valid option (1-2)\n")

    new_user_details = [new_username, new_password, 0, generate_acct_num(), "31-80-90", account_type]

    #Updates worksheet with new username if the username is unqiue
    print("\nAdding new user details to database...\n")
    user_worksheet = SHEET.worksheet("user-details")
    user_worksheet.append_row(new_user_details)

    #Creates new history worksheet for new user
    SHEET.add_worksheet(title=f"{new_username}-history", rows = 100, cols = 20)
    SHEET.worksheet(f"{new_username}-history").update_acell('A1', 'Date & Time')
    SHEET.worksheet(f"{new_username}-history").update_acell('B1', 'Details')
    SHEET.worksheet(f"{new_username}-history").update_acell('A2', str(time_now))
    SHEET.worksheet(f"{new_username}-history").update_acell('B2', 'New account created')
    print("Your new account has been created\n")
    print("Please restart the program and login.")


def generate_acct_num():
    all_acct_nums = SHEET.worksheet("user-details").col_values(4)

    while True:
        random_acct_num = randint(10000000, 99999999)
        existing_acct_num = any(x == random_acct_num for x in ALL_USERNAMES)

        if existing_acct_num == True:
            break
        else:
            return(random_acct_num)
            break


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
            
    # Throws error is password is not numbers
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

        print(f"\nLoading account...\n")

        #Update user history with action
        action = "User log in"
        update_user_history(existing_username, action)

        add_interest(existing_username, check_account_type(existing_username))

        main_menu(existing_username)
    else:
        print("Incorrect Details\n")
        existing_user_log_in()


def get_existing_login_details():
    """
    Returns all exisiting usernames and passwords as pairs in a dictonary.
    """
    existing_credentials = {ALL_USERNAMES: password for ALL_USERNAMES, password in zip(ALL_USERNAMES, ALL_PASSWORDS)}

    return existing_credentials


def validate_existing_login_details(username, password):
    """
    Validates user entered log in details against exisiting credentials in the spreadsheet.
    """
    existing_credentials = get_existing_login_details()
    correct_password = existing_credentials.get(username)

    if username in existing_credentials and correct_password == password:
        return True
    else:
        return False


def main_menu(username):
    """
    Main menu selection.
    """
    while True:
        print("\n***********************")
        print("Please select an option\n")
        print("1. Show Balance")
        print("2. Withdraw/Deposit Funds")
        print("3. Send Money")
        print("4. See Account History")
        print("5. Change Password")
        print("6. View Account Info")
        print("7. Exit")
        print("***********************\n")
        option = input("Please select an option (1-7):\n")

        if option == '1':
            show_balance(username)
            break
        elif option == '2':
            withdraw_deposit_funds_menu(username)
            break
        elif option == '3':
            send_money(username)
            break
        elif option == '4':
            call_user_history(username)
            break
        elif option == '5':
            change_password(username)
            break
        elif option == '6':
            call_user_acc_details(username)
            break
        elif option == '7':
            print("\nThank you for using Bank Of Sem. We hope you have a wonderful day.")
            break
        else: 
            print("\nPlease select a valid option (1-7)\n")


def show_balance(username):
    """
    Pairs all balances to the correct usernames then shows the balance assosiated with the 
    username used to log in.
    """

    print(f"\nLoading...\n")

    #Gets all exisiting usernames and pairs them to the correct balances in a dictionary
    all_balances = SHEET.worksheet("user-details").col_values(3)
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, all_balances)}
    balance = existing_balances.get(username)

    #Update user history with action
    action = "Viewed account balance"
    update_user_history(username, action)

    print(f"\nYour balance is: £{balance}\n")
    
    while True:
        print("\n***********************")
        print("1. Back")
        print("***********************\n")
        option = input("Please select an option:\n")
        if option == '1':
            main_menu(username)
            break
        else:
            print("\nPlease select a valid option\n")


def withdraw_deposit_funds_menu(username):
    """
    Withdraw/Deposit funds menu.
    """

    print(f"\nLoading...\n")

    #Gets all exisiting usernames and pairs them to the correct balances in a dictionary
    all_balances = SHEET.worksheet("user-details").col_values(3)
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, all_balances)}
    balance = existing_balances.get(username)

    print(f"\nYour balance is: £{balance}\n")

    while True:
        print("***********************")
        print("Please select an option\n")
        print("1. Deposit Funds")
        print("2. Withdraw Funds")
        print("3. Back")
        print("***********************\n")
        option = input("Please select an option (1-3):\n")

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
            print("\nPlease select a valid option (1-3)\n")


def deposit_funds(username):
    """
    Pairs all balances to the correct usernames then shows the balance assosiated with the 
    username used to log in. Allows the user to then add an amount to that balance and update
    the spreadsheet.
    """

    print(f"\nLoading...\n")

    #Gets all exisiting usernames and pairs them to the correct balances in a dictionary
    all_balances = SHEET.worksheet("user-details").col_values(3)
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, all_balances)}
    balance = existing_balances.get(username)
    username_cell = USER_DETAILS_SHEET.find(username)

    
    while True:
        print("\n***********************")
        deposit_amount = input("How much would you like to deposit?\n£")
        print("\n***********************")
        
        try:
            if int(deposit_amount) > 25000:
                print("There is a deposit limit of £25,000 per transaction. Please enter a lower deposit amount.\n")
            elif int(deposit_amount) < 25000:
                break
        except ValueError:
            print(f"Only numbers are accepted. Please try again.\n")

    # Calculates the new balance after deposit 
    new_balance = int(balance) + int(deposit_amount)

    while True:
        if check_account_type(username) != 'Growth Account':
            print("Depositing funds...\n")

            # Updates the users balance on the spreadsheet
            USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

            #Update user history with action
            action = f"Deposited £{deposit_amount} to account. Balance after deposit: £{new_balance}"
            update_user_history(username, action)

            print(f"Deposit complete. Your new balance is £{new_balance}\n")
            break

        elif int(new_balance) < 15000:
            print("Depositing funds...\n")

            # Updates the users balance on the spreadsheet
            USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

            #Update user history with action
            action = f"Deposited £{deposit_amount} to account. Balance after deposit: £{new_balance}"
            update_user_history(username, action)

            print(f"Deposit complete. Your new balance is £{new_balance}\n")
            balance_remaining = 15000 - new_balance
            print(f"You have £{balance_remaining} remaining of your £15,000 balance limit\n")
            break

        elif int(new_balance) > 15000:
            print("This account is a Growth Account and has a balance limit of £15000.")
            print("This deposit will cause your account to exceed the £15,000 limit.")
            print(f"Your current balance is: £{balance}. Please deposit a lower amount.\n")
            break

    while True:
        print("***********************")
        print("1. Back")
        print("***********************\n")
        option = input("Please select an option:\n")

        if option == '1':
            withdraw_deposit_funds_menu(username)
            break
        else:
            print("\nPlease select a valid option\n")

    all_balances = SHEET.worksheet("user-details").col_values(3)


def withdraw_funds(username):
    """
    Pairs all balances to the correct usernames then shows the balance assosiated with the 
    username used to log in. Allows the user to then withdraw an amount from that balance and update
    the spreadsheet. Wont allow more then the value of their exisiting balance to be withdrawn.
    """

    print(f"\nLoading...\n")

    all_balances = SHEET.worksheet("user-details").col_values(3)
    #Gets all exisiting usernames and pairs them to the correct balances in a dictionary
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, all_balances)}
    balance = existing_balances.get(username)
    username_cell = USER_DETAILS_SHEET.find(username)

    while True:
        print("\n***********************")
        withdraw_amount = input("How much would you like to withdraw?\n£")
        print("***********************\n")
        
        try:
            if int(withdraw_amount) > 25000:
                print("There is a withdrawl limit of £25,000 per transaction. Please enter a lower withdraw amount.\n")
            elif int(withdraw_amount) < 25000:
                break
        except ValueError:
            print(f"Only numbers are accepted. Please try again.\n")

    new_balance = int(balance) - int(withdraw_amount)
    
    # Throws message if withdraw amount is more then the available balance and wont allow the action 
    if int(withdraw_amount) > int(balance) or int(balance) == 0:

        action = f"Insufficient funds - Attemped to withdraw £{withdraw_amount} from account."
        update_user_history(username, action)

        print("Insufficient funds for withdrawal, please enter a lower amount\n")
    
        while True:
            print("***********************")
            print("1. Try again")
            print("2. Back")
            print("***********************")
            option = input("\nPlease select an option:\n")

            if option == '1':
                withdraw_funds(username)
                break
            elif option == '2':
                main_menu(username)
                break
            else:
                print("\nPlease select a valid option (1-2)\n")

    else:
        print("Withdrawing funds...\n")

        #Updates users balance on the spreadsheet after withdrawl
        USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)
        
        #Update user history with action
        action = f"Withdrew £{withdraw_amount} from account. Balance after deposit: £{new_balance}"
        update_user_history(username, action)

        print(f"Withdraw complete. Your new balance is £{new_balance}\n")
    
        while True:
            print("***********************")
            print("1. Back")
            print("***********************\n")
            option = input("Please select an option:\n")

            if option == '1':
                main_menu(username)
                break
            else:
                print("\nPlease select a valid option\n")

    all_balances = SHEET.worksheet("user-details").col_values(3)


def send_money(username):
    """
    Allows the user to withdraw money from their balance and deposit to another users.
    """

    print(f"\nLoading...\n")

    all_balances = SHEET.worksheet("user-details").col_values(3)
    all_account_types = SHEET.worksheet("user-details").col_values(6)
    #Gets all exisiting usernames and pairs them to the correct balances in a dictionary
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, all_balances)}
    existing_account_types = {ALL_USERNAMES: account_type for ALL_USERNAMES, account_type in zip(ALL_USERNAMES, all_account_types)}
    balance = existing_balances.get(username)
    account_type = existing_account_types.get(username)

    #Gets the location of the cell that matches the username 
    username_cell = USER_DETAILS_SHEET.find(username)

    user_option = input("Which user would you like to transfer to?\n")
    print("\nLocating user...\n")

    #Gets the location of the cell that matches the user they wish to transfer to
    selected_user_cell = USER_DETAILS_SHEET.find(user_option)
    existing_username = any(x == user_option for x in ALL_USERNAMES)

    selected_user_account_type = existing_account_types.get(user_option)

    #Checks if requested user exists in the spreadsheet
    if existing_username == True:

        #Checks if their account type
        if selected_user_account_type == "Growth Account":
            print("The selected users account is a Growth Account. Growth accounts are not able to transfer or recieve funds.")
            print("Please select another user.\n")

            while True:
                print("***********************")
                print("1. Try again")
                print("2. Back to main menu")
                print("***********************\n")
                option = input("Please select an option:\n")

                if option == '1':
                    send_money(username)
                    break
                elif option == '2':
                    main_menu(username)
                    break
                else:
                    print("\nPlease select a valid option (1-2)\n")

        amount_to_send = input("User found. How much would you like to transfer?\n£")
        
        #Calculates logged in users balance after withdraw amount has been selected
        new_balance = int(balance) - int(amount_to_send)

        #Gets the selected users balance before transfer & after transfer
        selected_user_balance = existing_balances.get(user_option)
        transfer_balance = int(selected_user_balance) + int(amount_to_send)

        #Throws a message if the transfer amount is more than available funds
        if int(amount_to_send) > int(balance) or int(balance) == 0:

            #Update user history with action
            action = f"Attempted to transfer £{amount_to_send} to {user_option}. Insufficient funds"
            update_user_history(username, action)

            print("\nInsufficient funds for transfer, please try again.\n")
            
            while True:
                print("***********************")
                print("1. Try again")
                print("2. Back to main menu")
                print("***********************\n")
                option = input("Please select an option:\n")

                if option == '1':
                    send_money(username)
                    break
                elif option == '2':
                    main_menu(username)
                    break
                else:
                    print("\nPlease select a valid option (1-2)\n")

        else:
            print("\nTransfering funds...\n")

            #Updates logged in users & selected users balance on the spreadsheet 
            USER_DETAILS_SHEET.update_cell(selected_user_cell.row, 3, transfer_balance)
            USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

            #Update user & selected user history with action
            action = f"Transfered £{amount_to_send} to {user_option}"
            update_user_history(username, action)
            action2 = f"Recieved £{amount_to_send} from {username}"
            update_user_history(user_option, action2)

            print(f"Transfer complete. Your new balance is £{new_balance}\n")

            while True:
                print("***********************")
                print("1. Back")
                print("***********************\n")
                option = input("Please select an option:\n")

                if option == '1':
                    main_menu(username)
                    break
                else:
                    print("\nPlease select a valid option\n")
    else:
        print("User does not exist. Please try again.\n")
        send_money(username)

    all_balances = SHEET.worksheet("user-details").col_values(3)


def next_available_row(worksheet):
    #From an external source (Please see README)
    str_list = list(filter(None, worksheet.col_values(1)))
    return str(len(str_list)+1)


def update_user_history(username, action):
    """
    Updates the logged in users history workseet with the last completed action
    """
    time_now = datetime.now()
    history_worksheet = SHEET.worksheet(f"{username}-history")
    next_row = next_available_row(history_worksheet)

    #From an external source (Please see README)
    history_worksheet.update_acell("A{}".format(next_row), str(time_now))
    history_worksheet.update_acell("B{}".format(next_row), action)


def call_user_history(username):
    """
    Calls the data in the logged in users history worksheet and returns it as a readable table
    """

    print(f"\nLoading...\n")

    history_worksheet = SHEET.worksheet(f"{username}-history")
    all_times = history_worksheet.col_values(1)
    all_history = history_worksheet.col_values(2)
    history_dict = {all_times: history for all_times, history in zip(all_times, all_history)}

    for time, history in history_dict.items():
        print(f'{time:19}  -  {history:40}')

    action = "Viewed account history"
    update_user_history(username, action)

    while True:
        print("\n***********************")
        print("1. Back")
        print("***********************\n")
        option = input("Please select an option:\n")

        if option == '1':
            main_menu(username)
            break
        else: 
            print("\nPlease select a valid option\n")


def change_password(username):
    """
    Change the exisiting password to a new one for the logged in user.
    Then updates the password in the database
    """

    print(f"\nLoading...\n")

    get_existing_login_details()

    username_cell = USER_DETAILS_SHEET.find(username)
    existing_credentials = get_existing_login_details()

    action = "Password changed."
    update_user_history(username, action)

    while True:
        print("***********************\n")
        new_password = input("Please enter in a new password. It must be 4 numbers:\n")
        
        if validate_new_password(new_password):
            break
    
    print("\nUpdating your password...\n")
    USER_DETAILS_SHEET.update_cell(username_cell.row, 2, new_password)
    print("Password successfully updated\n")
    print("Please restart the program and login.")


def call_user_acc_details(username):
    """
    Calls and shows the user details data for the logged in user
    """

    print(f"\nLoading...\n")

    username_cell = USER_DETAILS_SHEET.find(username)
    row_headings = USER_DETAILS_SHEET.row_values(1)
    username_row_data = USER_DETAILS_SHEET.row_values(username_cell.row)
    acc_details_dict = {heading: data for heading, data in zip(row_headings, username_row_data)}

    for heading, data in acc_details_dict.items():
        if heading == 'Password':
            print(f'{heading:15}  -  ****')
        elif heading != 'Balance':
            print(f'{heading:15}  -  {data}')
        else:
            print(f'{heading:15}  -  £{data}')

    action = "Account information viewed."
    update_user_history(username, action)

    while True:
        print("\n***********************")
        print("1. Back")
        print("***********************\n")
        option = input("Please select an option:\n")

        if option == '1':
            main_menu(username)
            break
        else: 
            print("\nPlease select a valid option\n")


def check_account_type(username):
    """
    Checks and returns the users account type.
    """
    username_cell = USER_DETAILS_SHEET.find(username)
    user_account_type = USER_DETAILS_SHEET.cell(username_cell.row, 6).value

    return user_account_type


def add_interest(username, account):
    """
    Adds 1% interest to the users balance and updates the spreadsheet
    """
    all_balances = SHEET.worksheet("user-details").col_values(3)
    existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES, balance in zip(ALL_USERNAMES, all_balances)}
    balance = existing_balances.get(username)
    username_cell = USER_DETAILS_SHEET.find(username)

    if account == 'Growth Account':
        new_balance = int(balance) + round((int(balance) * 0.01))
        USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

        #Update user history with action
        action = f"1% interest added to balance. Balance after interest gained: £{new_balance}"
        update_user_history(username, action)
    else:
        pass


def main():
    """
    Run all program functions.
    """
    user_log_in()


main()