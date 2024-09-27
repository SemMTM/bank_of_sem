class Bank_Account:
    def __init__(self, username):
        self.username = username


    def show_balance(self):
        """
        Pairs all balances to the correct usernames then shows the balance
        assosiated with the username used to log in.
        """
        print(f"\nLoading...\n")

        # Gets all exisiting usernames and pairs them to the correct
        # balances in a dictionary
        all_balances = SHEET.worksheet("user-details").col_values(3)
        existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES,
                            balance in zip(ALL_USERNAMES, all_balances)}
        balance = existing_balances.get(self.username)

        print("\n***********************")
        print(f"Your balance is: £{balance}\n")
        print("***********************\n")

        # Update user history with action
        action = "Viewed account balance"
        Customer_Account(self.username).update_user_history(action)

        while True:
            option = input("Press any key to continue:\n")
            if option == option:
                main_menu(self.username)
                break


    def deposit_funds(self):
        """
        Pairs all balances to the correct usernames then shows the balance
        assosiated with the username used to log in. Allows the user to
        then add an amount to that balance and update the spreadsheet.
        """
        print(f"\nLoading...\n")

        # Gets all exisiting usernames and pairs them to the
        # correct balances in a dictionary
        all_balances = SHEET.worksheet("user-details").col_values(3)
        existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES,
                            balance in zip(ALL_USERNAMES, all_balances)}
        balance = existing_balances.get(self.username)
        username_cell = USER_DETAILS_SHEET.find(self.username)

        while True:
            print("\n***********************")
            deposit_amount = input("How much would you like to deposit?\n£")
            print("\n***********************")

            try:
                if int(deposit_amount) < 0:
                    print(Fore.RED + "Please enter a positive figure.\n")
                elif int(deposit_amount) > 25000:
                    print(Fore.RED + "There is a deposit limit of £25,000 "
                        "per transaction. "
                        "Please enter a lower deposit amount.\n")
                elif int(deposit_amount) < 25000:
                    break
            except ValueError:
                print(Fore.RED + f"Only numbers are accepted. Please try again.\n")

        # Calculates the new balance after deposit
        new_balance = int(balance) + int(deposit_amount)

        while True:
            if check_account_type(self.username) != 'Growth Account':
                print("Depositing funds...\n")

                # Updates the users balance on the spreadsheet
                USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

                # Update user history with action
                action = f"Deposited £{deposit_amount} to account. "
                f"Balance after deposit: £{new_balance}"
                Customer_Account(self.username).update_user_history(action)

                print(Fore.GREEN + "Deposit complete.")
                print(f"Your new balance is £{new_balance}.\n")
                break

            elif int(new_balance) < 15000:
                print("Depositing funds...\n")

                # Updates the users balance on the spreadsheet
                USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

                # Update user history with action
                action = f"Deposited £{deposit_amount} to account. "
                f"Balance after deposit: £{new_balance}"
                Customer_Account(self.username).update_user_history(action)

                print(Fore.GREEN + "Deposit complete.")
                print(f"Your new balance is £{new_balance}.\n")
                balance_remaining = 15000 - new_balance
                print(f"You have £{balance_remaining} remaining of "
                    "your £15,000 balance limit\n")
                break

            elif int(new_balance) > 15000:
                print(Fore.RED + "This account is a Growth Account and has a "
                    "balance limit of £15000.")
                print(Fore.RED + "This deposit will cause your account "
                    "to exceed the £15,000 limit.")
                print(Fore.RED + f"Your current balance is: £{balance}. "
                    "Please deposit a lower amount.\n")
                break

        while True:
            option = input("\nPress any key to continue:\n")

            if option == option:
                withdraw_deposit_funds_menu(self.username)
                break

    
    def withdraw_funds(self):
        """
        Pairs all balances to the correct usernames then shows the balance
        assosiated with the username used to log in. Allows the user to then
        withdraw an amount from that balance and update the spreadsheet.
        Wont allow more then the value of their exisiting balance to be withdrawn.
        """
        print(f"\nLoading...\n")

        all_balances = SHEET.worksheet("user-details").col_values(3)

        # Gets all exisiting usernames and pairs them to the correct balances in
        # a dictionary
        existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES,
                            balance in zip(ALL_USERNAMES, all_balances)}
        balance = existing_balances.get(self.username)
        username_cell = USER_DETAILS_SHEET.find(self.username)

        while True:
            print("\n***********************")
            withdraw_amount = input("How much would you like to withdraw?\n£")
            print("***********************\n")

            try:
                if int(withdraw_amount) < 0:
                    print(Fore.RED + "Please enter a positive figure.\n")
                elif int(withdraw_amount) > 25000:
                    print(Fore.RED + "There is a withdrawl limit of £25,000 per "
                        "transaction. Please enter a lower withdraw amount.\n")
                elif int(withdraw_amount) < 25000:
                    break
            except ValueError:
                print(Fore.RED + f"Only numbers are accepted. Please try again.\n")

        new_balance = int(balance) - int(withdraw_amount)

        # Throws message if withdraw amount is more then the available balance
        # and wont allow the action
        if int(withdraw_amount) > int(balance) or int(balance) == 0:

            action = "Insufficient funds - Attemped to withdraw "
            f"£{withdraw_amount} from account."
            Customer_Account(self.username).update_user_history(action)

            print(Fore.RED + "Insufficient funds for withdrawal, "
                "please enter a lower amount\n")

            while True:
                print("***********************")
                print("1. Try again")
                print("2. Back")
                print("***********************")
                option = input("\nPlease select an option:\n")

                if option == '1':
                    withdraw_funds(self.username)
                    break
                elif option == '2':
                    main_menu(self.username)
                    break
                else:
                    print(Fore.RED + "\nPlease select a valid option (1-2)\n")

        else:
            print("Withdrawing funds...\n")

            # Updates users balance on the spreadsheet after withdrawl
            USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

            # Update user history with action
            action = f"Withdrew £{withdraw_amount} from account. "
            f"Balance after deposit: £{new_balance}"
            Customer_Account(self.username).update_user_history(action)

            print(Fore.GREEN + "Withdraw complete.\n")
            print(f"Your new balance is £{new_balance}.\n")

            while True:
                option = input("\nPress any key to continue:\n")

                if option == option:
                    withdraw_deposit_funds_menu(self.username)
                    break

    
    def send_money(self):
        """
        Allows the user to withdraw money from their balance and
        deposit to another users.
        """
        print(f"\nLoading...\n")

        all_balances = SHEET.worksheet("user-details").col_values(3)
        all_account_types = SHEET.worksheet("user-details").col_values(6)

        # Gets all exisiting usernames and pairs them to the correct balances
        # in a dictionary
        existing_balances = {ALL_USERNAMES: balance for ALL_USERNAMES,
                            balance in zip(ALL_USERNAMES, all_balances)}
        existing_account_types = {ALL_USERNAMES: account_type for ALL_USERNAMES,
                                account_type in zip(ALL_USERNAMES,
                                                    all_account_types)}
        balance = existing_balances.get(self.username)
        account_type = existing_account_types.get(self.username)

        # Gets the location of the cell that matches the username
        username_cell = USER_DETAILS_SHEET.find(self.username)

        user_option = input("Which user would you like to transfer to?\n")
        print("\nLocating user...\n")

        # Gets the location of the cell that matches the user they wish to
        # transfer to
        selected_user_cell = USER_DETAILS_SHEET.find(user_option)
        existing_username = any(x == user_option for x in ALL_USERNAMES)
        selected_user_account_type = existing_account_types.get(user_option)

        # Checks if requested user exists in the spreadsheet
        if existing_username is True:

            # Checks if their account type
            if selected_user_account_type == "Growth Account":
                print("The selected users account is a Growth Account. "
                    "Growth accounts are not able to transfer or recieve funds.")
                print("Please select another user.\n")

                while True:
                    print("***********************")
                    print("1. Try again")
                    print("2. Back to main menu")
                    print("***********************\n")
                    option = input("Please select an option:\n")

                    if option == '1':
                        self.send_money()
                        break
                    elif option == '2':
                        main_menu(self.username)
                        break
                    else:
                        print(Fore.RED + "\nPlease select a valid option (1-2)\n")

            while True:
                amount_to_send = input("User found. How much would "
                                    "you like to transfer?\n£")
                try:
                    if int(amount_to_send) < 0:
                        print(Fore.RED + "You cannnot withdraw funds from another "
                            "users account. Please try again.\n")
                    elif int(amount_to_send) > 25000:
                        print(Fore.RED + "There is a transfer limit of £25,000 "
                            "per transaction.")
                        print(Fore.RED + "Please enter a lower withdraw amount.\n")
                    elif int(amount_to_send) < 25000:
                        break
                except ValueError:
                    print(Fore.RED + f"Only numbers are accepted. "
                                    "Please try again.\n")

            new_balance = int(balance) - int(amount_to_send)

            # Gets the selected users balance before transfer & after transfer
            selected_user_balance = existing_balances.get(user_option)
            transfer_balance = int(selected_user_balance) + int(amount_to_send)

            # Throws a message if the transfer amount is more than available funds
            if int(amount_to_send) > int(balance) or int(balance) == 0:

                # Update user history with action
                action = f"Attempted to transfer £{amount_to_send} "
                f"to {user_option}. Insufficient funds"
                Customer_Account(self.username).update_user_history(action)

                print(Fore.RED + "\nInsufficient funds for transfer, "
                                "please try again.\n")

                while True:
                    print("***********************")
                    print("1. Try again")
                    print("2. Back to main menu")
                    print("***********************\n")
                    option = input("Please select an option:\n")

                    if option == '1':
                        self.send_money()
                        break
                    elif option == '2':
                        main_menu(self.username)
                        break
                    else:
                        print(Fore.RED + "\nPlease select a valid option (1-2)\n")

            else:
                print("\nTransfering funds...\n")

                # Updates logged in users & selected users balance on
                # the spreadsheet
                USER_DETAILS_SHEET.update_cell(selected_user_cell.row,
                                            3, transfer_balance)
                USER_DETAILS_SHEET.update_cell(username_cell.row, 3, new_balance)

                # Update user & selected user history with action
                action = f"Transfered £{amount_to_send} to {user_option}"
                Customer_Account(self.username).update_user_history(action)
                action2 = f"Recieved £{amount_to_send} from {self.username}"
                Customer_Account(user_option).update_user_history(action2)

                print(Fore.GREEN + "Transfer complete.")
                print(f"Your new balance is £{new_balance}\n")

                while True:
                    option = input("\nPress any key to continue:\n")

                    if option == option:
                        main_menu(self.username)
                        break
        else:
            print(Fore.RED + "User does not exist. Please try again.\n")
            self.send_money()