class Customer_Account:
    time_now = datetime.now()

    def __init__(self, username):
        self.username = username

    def account_create(self, password, account_type):
        self.password = password
        self.account_type = account_type
        new_user_details = [self.username, self.password, 0, generate_acct_num()
                            , '31-80-90', self.account_type]

        # Updates worksheet with new username if the username is unqiue
        print("\nAdding new user details to database...\n")
        user_worksheet = SHEET.worksheet("user-details")
        user_worksheet.append_row(new_user_details)

        # Creates new history worksheet for new user
        SHEET.add_worksheet(title=f"{self.username}-history", rows=100, cols=20)
        SHEET.worksheet(f"{self.username}-history").update_acell('A1',
                                                                'Date & Time')
        SHEET.worksheet(f"{self.username}-history").update_acell('B1', 'Details')
        SHEET.worksheet(f"{self.username}-history").update_acell('A2',
                                                                str(self.time_now))
        SHEET.worksheet(f"{self.username}-history").update_acell('B2',
                                                                'New account '
                                                                'created')
        print(Fore.GREEN + "Your new account has been created\n")
        print("Please restart the program and login.")


    def exisiting_log_in(self, password):
        self.password = password

        if validate_existing_login_details(self.username, self.password):
            print(Fore.GREEN + "Correct Login Details\n")

            print(f"\nLoading account...\n")

            # Update user history with action
            action = "User log in"
            self.update_user_history(action)

            add_interest(self.username, check_account_type(self.username))

            main_menu(self.username)
        else:
            print(Fore.RED + "Incorrect Details\n")
            existing_user_log_in()

    
    def update_user_history(self, action):
        self.action = action

        """
        Updates the logged in users history workseet with the last completed action
        """
        history_worksheet = SHEET.worksheet(f"{self.username}-history")
        next_row = next_available_row(history_worksheet)

        # From an external source (Please see README)
        history_worksheet.update_acell("A{}".format(next_row), str(self.time_now))
        history_worksheet.update_acell("B{}".format(next_row), action)

    
    def password_change(self):
        """
        Change the exisiting password to a new one for the logged in user.
        Then updates the password in the database
        """

        print(f"\nLoading...\n")

        username_cell = USER_DETAILS_SHEET.find(self.username)

        action = "Password changed."

        while True:
            print("***********************\n")
            new_password = pwinput.pwinput(prompt="Please enter in a new "
                                           "password. It must be 4 numbers:\n")
            if validate_new_password(new_password):
                break  

        print("\nUpdating your password...\n")
        USER_DETAILS_SHEET.update_cell(username_cell.row, 2, new_password)
        self.update_user_history(action)  
        print(Fore.GREEN + "Password successfully updated\n")
        print("Please restart the program and login.")

    
    def call_user_history(self):
        """
        Calls the data in the logged in users history worksheet and returns
        it as a readable table
        """
        print(f"\nLoading...\n")

        history_worksheet = SHEET.worksheet(f"{self.username}-history")
        all_times = history_worksheet.col_values(1)
        all_history = history_worksheet.col_values(2)
        history_dict = {all_times: history for all_times,
                        history in zip(all_times, all_history)}

        for time, history in history_dict.items():
            print(f'{time:19}  -  {history:40}')

        action = "Viewed account history"
        self.update_user_history(action)

        while True:
            option = input("\nPress any key to continue:\n")

            if option == option:
                main_menu(self.username)
                break

    
    def call_user_acc_details(self):
        """
        Calls and shows the user details data for the logged in user
        """
        print(f"\nLoading...\n")

        username_cell = USER_DETAILS_SHEET.find(self.username)
        row_headings = USER_DETAILS_SHEET.row_values(1)
        username_row_data = USER_DETAILS_SHEET.row_values(username_cell.row)
        acc_details_dict = {heading: data for heading,
                            data in zip(row_headings, username_row_data)}

        for heading, data in acc_details_dict.items():
            if heading == 'Password':
                print(f'{heading:15}  -  ****')
            elif heading != 'Balance':
                print(f'{heading:15}  -  {data}')
            else:
                print(f'{heading:15}  -  £{data}')

        action = "Account information viewed."
        self.update_user_history(action)

        while True:
            option = input("\nPress any key to continue:\n")

            if option == option:
                main_menu(self.username)
                break
