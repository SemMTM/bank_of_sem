# Bank Of Sem
## A Terminal Based Banking Application
A terminal based banking application that is connected to a databased via api and updates the information based on user action. To use the application, a user must create an account with a unique username & 4 digit password, thesse are then pushed to the data base. To log in, the user must use the correct & matching credentials or access to the account will be denied.

The user can do a variety of banking based tasks once logged in, these are:
1. Show Balance
2. Withdraw/Deposit Funds
3. Send Money To Another User
4. See Account History
5. Change Password
6. View Account Info
7. Exit

Every action will be pushed to the database and updated.

#### The Purpose:
The purpose of this application is to allow a user to securely create & manage their account with the Bank Of Sem while having the ability to use many of the features you would expect to have on a banking application. 

#### Target Audience:
The target audience for this app would be anyone who needs a secure way to store & manage their finances.

#### Live site: https://bank-of-sem-cd1ad5a802b4.herokuapp.com
Please use the following log in details to use the app:
- Username: User2
- Password: 9999

List of other users to test transfer feature:
- SemMTM
- User3
- User4

#### Repository: https://github.com/SemMTM/bank_of_sem

## Table of Contents
1. UX
2. Features
3. Future Features
4. Technology Used 
5. Testing
6. Bugs
7. Credits
8. Deployment

## 1. Pre-project Planning
The plan for this project was to create a terminal based banking application that would manipulate data stored in a database. All users would have unique usernames and passwords that could be changed by the user. I wanted to imitate a real banking applications features as much as possible. Every action should cause some change in the database. 

The pre planned features were:
1. Change password
2. See balance
3. Withdraw/Deposit funds
4. Send money to another user in the database
5. The ability to see a history of all actions taken on the account

### 1.2. UX Design
As I had quite a few features planned and this was a terminial based program, the user needs a way to easily navigate back an forth between all the features. The user would select their options from a predetermined & numbered option list. Each selection will provide the user with some kind of response and relevant sub-options. 

The main structure structure would be as follows:
1. A log in screen with the following options:
  - Log in
  - Create account

2. A main menu with a list of the main features and an exit option:
  - Option 1
  - Option 2
  - Option 3
  - Option 4
  - Exit

Each main option will then either prompt a user input for data to be submitted to the database or there will be a sub menu to further specify what action they would like to take. After an action has been completed, the user will be prompted with a back option if they wish to continue with more tasks.

### 1.3. User Stories
- First Time Visitor Goals
  - As a first time visitor, I want to create an account
  - As a first time visitor, I want to deposit money into my new account
  - As a first time visitor, I want to see all available features quickly

- Returning Visitor Goals
  - As a returning visitor, I want to be able to withdraw funds from my account
  - As a returning visitor, I want to be see my available balance
  - As a returning visitor, I want to be able to log in with my newly created account

- Frequent User Goals:
  - As a frequent user, I want to be able to send money to another user
  - As a frequent user, I want to be able to change my password 
  - As a frequent user, I want to be able to see my account activity 
  - As a frequent user, I want to be able to see my account information

### 1.4. Flow Charts

## 2. Features
### Main Menu
- Welcomes the user to the Bank Of Sem and introduces the 2 main options.
- Prompts the user to make a selection.

![Main menu](<assets/readme images/Screenshot_2.png>)

- Throws and error if an invalid option is selected.

![Wrror message](<assets/readme images/Screenshot_1.png>)

### Create Account
- Username
  - Allows the user to create an account that will be pushed to the database. Each username must be unique or an error will be thrown.

![Enter username screen](<assets/readme images/Screenshot_4.png>)

- Password
  - Once a unique username has been selected, the user will be promted to input a 4 digit password.
  - The password must be 4 numbers or an error will be thrown.

![Enter password error message](<assets/readme images/Screenshot_5.png>)

- Account Type
  - After a valid password has been chosen, the user will be prompted to select an account type.
  - Each account may only be 1 account type. Certain account types have different benefit & restrictions.
  - Current accounts function like a regular bank account and have no restrictions.
  - Growth accounts have a £15,000 deposit limit, can't be sent money and gain 1% interest on every log in. This interest is pushed to the database after it is calculated.

![Account type selection](<assets/readme images/Screenshot_6.png>)

- Account creation in database
  - Once all options have been selected, the new user details will then be pushed to the database.
  - The user will be prompted while this happens.
  - Validation will be done against these details for future log ins and the account type will have an effect on the functions of the account.

![New user being created](<assets/readme images/Screenshot_7.png>)

  - Once an account is created the username, password and account type are pushed to the database.
  - A random account number is generated, a sortcode and a balance of £0.
  - A user history page is also created. This page logs all future actions of the user once logged in.

![New user in datavase](<assets/readme images/Screenshot_8.png>)

![New user history tab](<assets/readme images/Screenshot_9.png>)

![New user history](<assets/readme images/Screenshot_10.png>)

### Log In
- To log in, the details provided must match the details in the database or access will be denied.
- Usernames and passwords are paired and if the entered details do not match a pair, then an error will be thrown.

![Incorrect log in details](<assets/readme images/Screenshot_11.png>)

- Once the correct details are entered, the user will be shown a "loading account..." message and be taken to a main menu.

![Log in details in spreadsheet](<assets/readme images/Screenshot_14.png>)

![Correct log in details](<assets/readme images/Screenshot_12.png>)

### Main Menu
- The main menu shows the user all of the actions that can be taken on their account.
- If an invalid option is selected, then an error message is thrown.

![Main Menu](<assets/readme images/Screenshot_13.png>)

### Show Balance
- This option extracts the logged in users balance from the list of users in the spreadsheet and displays it in the terminal.

![User balance in speadsheet](<assets/readme images/Screenshot_14.png>)

![User balance in terminal](<assets/readme images/Screenshot_15.png>)

### Withdraw/Deposit Funds
- A user is able to withdraw/deposit funds from their account.

![Withdraw/deposit funds menu](<assets/readme images/Screenshot_16.png>)

- Deposit funds
  - The amount a user can deposit depends on their account type.
  - A current account has an unlimited deposit limit.
  - A growth account has a max deposit of £15,000.

  ![Deposit limit for growth accounts](<assets/readme images/Screenshot_17.png>)

  - Upon a successful deposit, a message with the new account balance will be displayed to the user and the amount will be added to the balance on the spreadsheet.
  - If the account is a growth account then a message telling them their remaining deposit amount of their £15,000 limit.

  ![successful deposit](<assets/readme images/Screenshot_19.png>)

  ![spreadsheet updated with deposit amount](<assets/readme images/Screenshot_20.png>)

- Withdraw funds
  - The user can't withdraw more money then they have in their account.

  ![insufficient funds for withdrawl message](<assets/readme images/Screenshot_18.png>)

  - After a successful withdrawl, the user is shown a message with their new balance and the spreadsheet is updated.

  ![Successful withdrawl](<assets/readme images/Screenshot_21.png>)

  ![Successful withdrawl update in spreadsheet](<assets/readme images/Screenshot_22.png>)

### Send Money To Another User
- A user must exist to be able to send money. If a non-existant user to selected then an error message will be thrown.

![Non existant user error message](<assets/readme images/Screenshot_23.png>)

- Once an existing user is selected, the user will recieve a "user found" message. The transfer will start and the specifed amount will be taken from the logged in users balance and added to the selected users balance. A message is shown to display the logged in users balance after the transfer.

![successful transfer](<assets/readme images/Screenshot_24.png>)

- The logged in users and selected users balances are updated in the spreadsheet.

![successful transfer updated in spreadsheet](<assets/readme images/Screenshot_25.png>)

- Funds cannot be sent to Growth Accounts. An error message will be displayed if the logged in user tries to send money to a user with a growth account.

![Message when trying to transfer to growth account](<assets/readme images/Screenshot_26.png>)

- A user cannnot send more money then their available funds. If they try to do this, an error message will be thrown.

![Message when trying to transfer more than available funds](<assets/readme images/Screenshot_27.png>)

### See Account History
- Every action on a logged in users account is saved and time stamped in the users "history" tab.
- These actions are pushed to the database and can be called & displayed in the terminal.
- The data has been formatted to be more readable for the user.

![View account history in terminal](<assets/readme images/Screenshot_28.png>)

![View account history in database](<assets/readme images/Screenshot_29.png>)

### Change Password
- The logged in user can change the password associated with their account.
- The changing password follows the same validation as creating one at log in. It must be 4 numbers only and will throw an error if not.

![Change password error](<assets/readme images/Screenshot_30.png>)

- After the new password is created, the database will be updated and the user must use this new password to log in to their account in the future.

![Change password updated](<assets/readme images/Screenshot_31.png>)

![Change password updated in database](<assets/readme images/Screenshot_32.png>)
  

## 3. Future Features

## 4. Technology Used
### Python

### Gspread

## 5. Testing
For all testing please refer to the TESTING.md file.

## 6. Bugs
### 6.1. Fixed Bugs

### 6.2. Unfixed Bugs

## 7. Credits

### 7.1. Content & Resources
- How to use any() to check if an element exists in a list: https://www.analyticsvidhya.com/blog/2024/02/check-if-element-exists-in-list-in-python/#:~:text=Using%20the%20%27any()%27%20Function,-The%20%27any()&text=You%20can%20determine%20if%20it,"Element%20not%20found."%20)&text=Element%20found!,-Using%20the%20%27count
- Used validate_data function from the Love Sandwiches project
- How to populate the next empty cell in a col with a specifed value: https://stackoverflow.com/questions/40781295/how-to-find-the-first-empty-row-of-a-google-spread-sheet-using-python-gspread
- How to generate a random number of digits: https://stackoverflow.com/questions/2673385/how-to-generate-a-random-number-with-a-specific-amount-of-digits

### 7.3. Acknowledgements

## 8. Deployemnt