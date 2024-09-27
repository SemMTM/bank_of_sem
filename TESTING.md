# **Testing**
## **5.1. Developer Testing**

| **Feature** | **What we are testing** | **How we test it** | **What we expect to happen** | **Result** |
|--|--|--|--|--|
| **Top Menu** |  |  |  | 
|  | Top menu load as expected on program load | Click "Run Program" button on terminal application | Welcome message and top menu loads | Pass
|  | Error message is thrown if invalid option selected | Type a number of different characters != 1 or 2 | Error message is thrown | Pass
|  | Option sub-menus load correctly when selected  | Type 1, then reload and type 2 to test all options | Options load correctly and prompt the user | Pass
| **Log In** |  |  |  | 
|  | Log in validation functions as expected | Enter incorrect username or password | "incorrect Details" message is thrown and user is prompted to re-enter details | Pass
|  | Log in can only be successful if details match an existing username & password pair in the database | Enter an exisiting username and password pair | Successful log in | Pass
|  | Log in will be unsuccessful if details do not match an existing username & password pair in the database | Enter an exisiting username with a different usernames password | "incorrect Details" message is thrown and user is prompted to re-enter details | Pass
|  | Log in will be unsuccessful if no information is entered | Enter no information | "incorrect Details" message is thrown and user is prompted to re-enter details | Pass
|  | Users history updated with log in details after successful log in| Log in to Test user | Test users history tab has been updated with log in time | Pass
| **Create Account** |  |  |  | 
|  | Entered username must be unique | Enter username "Test" as this username already exists within the database | Error message is thrown and user is prompted to enter a new username | Pass
|  | An accepted username allows user to continue account creation | Enter username "Test2" as this username is unique | User is allowed to enter a new password | Pass
|  | Password must only be 4 numbers | Enter 3 numbers | Error message is thrown and user is prompted to enter a new password | Pass
|  | Password must only be 4 numbers | Enter 4 letters | Error message is thrown and user is prompted to enter a new password | Pass
|  | Error thrown when user option != 1 or 2 in account type selection | Enter number 4 | Error message is thrown and user is prompted to reselect account type | Pass
|  | Error thrown when user option != 1 or 2 in account type selection | Enter letter a | Error message is thrown and user is prompted to reselect account type | Pass
|  | New account details are pushed to database | Enter username "Test2" as this username is unique, password "1234", account type 1 | Database updates with new details and user is promted to restart the program | Pass
|  | User can log in with new details after program restart | Log in with the following details: Username: Test2 Password: 1234 | User is taken to main menu | Pass
|  | A new user history tab has been created with the new users name | Check database for a worksheet with the name "Test2-history" | Tab "Test2-history" has been created | Pass
|  | A random account & unique number has been generated and assigned to the user | Check user "Test2" details in the database and see if account number has been generated and is unqiue | Account number is unique and has been assigned to the correct user | Pass
|  | The new users details have appended under the last created users details | Check user "Test2" details have not overwritten another users details" | Details have appended correctly | Pass
| **Main Menu** |  |  |  | 
|  | Option "1. Show Balance" opens relevant sub menu | Select option 1. | User is shown their available balance | Pass
|  | Option "2 Withdraw/Deposit Funds" opens relevant sub menu | Select option 2. | User is showns withdraw/deposit sub menu | Pass
|  | Option "3. Send Money" opens relevant sub menu | Select option 3. | Ask user who they want to send money to | Pass
|  | Option "4. See Account History" opens relevant sub menu | Select option 4. | Loads users account history with times | Pass
|  | Option "5. Change Password" opens relevant sub menu | Select option 5. | Prompts user to enter new password | Pass
|  | Option "6. View Account Info" opens relevant sub menu | Select option 6. | Displays correct users account info | Pass
|  | Option "7. Exit" displays goodbye message and closes app | Select option 7. |  | Pass
|  | Error message is thrown if invalid option selected | Type a number of different characters != 1 or 2 | Error message is thrown and user is promted to select another option | Pass
| **Show Balance** |  |  |  | 
|  | The user is shown their balance | Press option 1. in the main menu | A Balance that matches the logged in users balance in the spreadsheet is displayed | Pass
|  | "Press any key to continue" operates as expected | After balance is shown, type any key. Test with multiple different keys. | Key press takes the user back to main menu | Pass on every key tested
|  | Users history tab updated with show balance details after balance is viewed | View balance | Logged in users history tab is updated with the time balance was viewed | Pass
| **Withdraw/Deposit Funds** |  |  |  | 
| *Deposit Function* |  |  |  | 
|  | Users balance is displayed above menu selection | Check the balance shown against users detail in the spreadsheet matches balance displayed | Both balances match (in the spreadsheet and shown above menu) | Pass
|  | User is promted to add deposit amount | Press option 1. in the sub-menu | User is promted to add deposit amount | Pass
|  | Users can add funds to their balance | Add a deposit amount of 500 | Balance is incremented by 500 | Pass
|  | New balance is pushed to spreadsheet | Add a deposit amount of 500 | Users balance on spreadsheet matches new balance specified in terminal after deposit | Pass
|  | Deposit amount cannot be left blank | leave deposit amount blank | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | Balance shown in terminal after deposit is accurate | Set test user balance to 1000. Deposit 500. | Balance shown in terminal should be 1500 | Pass
|  | A user cannot deposit more than 25000 per transaction | Add a deposit amount of 30000 | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | A growth account cannot be deposited more than their £15,000 limit | Log in with a growth account, deposit more then their remaining available limit | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | Only numbers can be entered as a valid deposit amount | Enter the letter 'a' as deposit amount | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | Users history tab updated with deposit details after successful transaction | Deposit £399 | Logged in users history tab is updated with deposit time and amount | Pass
|  | "Press any key to continue" operates as expected | After deposit, type any key. Test with multiple different keys. | Key press takes the user back to main menu | Pass on every key tested
| *Withdraw Function* |  |  |  | 
|  | User is promted to type a withdraw amount | Press option 2. in the sub-menu | User can type a withdraw amount | Pass
|  | Users can withdraw funds from their available balance | Withdraw 500 | Balance is reduced by 500 | Pass
|  | New balance is pushed to spreadsheet | Withdraw 500 | Users balance on spreadsheet matches new balance specified in terminal after withdrawl | Pass
|  | Balance shown in terminal after withdrawl is accurate | Set test users balance to 1000. withdraw 500. | Balance shown in terminal should be 500 | Pass
|  | Withdraw amount cannot be left blank | Leave withdraw amount blank | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | A user cannot withdraw more than 25000 per transaction | Attempt to withdraw 30000 | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | A user cannot withdraw more than their available balance | Attempt to withdraw more than logged in users available balance | Insufficient funds error message is thrown and user is prompted to re-enter an amount | Pass
|  | Only numbers can be entered as a valid withdrawl amount | Enter the letter 'a' as withdrawl amount | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | Users history tab updated with withdrawl details after successful transaction | Withdraw £399 | Logged in users history tab is updated with withdraw time and amount | Pass
|  | "Press any key to continue" operates as expected | After withdraw, type any key. Test with multiple different keys. | Key press takes the user back to main menu | Pass on every key tested
| **Send Money** |  |  |  | 
|  | User is prompted to input a username to send money to | Press option 3. from the main menu | User is propmted to type a username | Pass
|  | Username validation for exisiting users functions as expected | Enter a non-existant username | Error message "User does not exist" is thrown and user is prompted to re-enter a name | Pass
|  | Exisiting users are found by the program & paired to the correct balance | Type user "SemMTM" and send user 10  | User found message is thown and SemMTMs balance in spreadhseet is increased by 10 |
|  | Transfer amount is subtracted from logged users balance and added to selected users balance | Send 10 to a selected user | Logged in users balance decreased by 10, selected users balance increased by 10 in the database |
|  | A user cannot transfer more then their available balance | Attempt to send more than available balance to a user | Insufficient funds error message is thrown and user is prompted to re-enter an amount | Pass
|  | A Growth Account cannot be transfered to | Attempt to send money to a user with a Growth Account | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | Only numbers can be entered as a valid transfer amount | Enter the letter 'a' as transfer amount | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | Users history tab updated with transfer details after successful transaction | Transfer 400 to User2 | Logged in users history tab is updated with transfer details | Pass
|  | Transferred to user's history tab updated with transfer details after successful transaction | Transfer 400 to User2 | Logged in users history tab is updated with transfer details | Pass
|  | User cannot enter negative amount for transfer | Attempt to transfer -100 to another user | Error message is thrown and user is prompted to try again | Pass
|  | A user cannot transfer more than 25000 per transaction | Attempt to transfer 30000 | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | "Press any key to continue" operates as expected | After transfer, type any key. Test with multiple different keys. | Key press takes the user back to main menu | Pass on every key tested
|  | Transfer amount cannot be left blank | Leave transfer amount blank | Error message is thrown and user is prompted to re-enter an amount | Pass
| **See Account History** |  |  |  | 
|  | Account actions are published with the correct date and time | Select "See Account History" and compare what is shown in termal to users history tab in database | All user hisotry times and dates match database | Pass
|  | Account history is formatted as expected | Select "See Account History" | Account history is formatted as expected | Pass
|  | Users account history pulled from database with the correct information | Select "See Account History" and compare what is shown in termal to users history tab in database | Information pulled up in termal matches history tab for logged in user | Pass
|  | "Press any key to continue" operates as expected | After account history is shown, type any key. Test with multiple different keys. | Key press takes the user back to main menu | Pass on every key tested
|  | Error message is thrown if invalid option selected after view history | Type a number of different characters != 1 | Error message is thrown and user is promted to select another option | Pass
| **Change Password** |  |  |  | 
|  | New password must only be 4 numbers | Enter 3 numbers | Error message is thrown and user is prompted to enter a new password | Pass
|  | New password must only be 4 numbers | Enter 4 letters | Error message is thrown and user is prompted to enter a new password | Pass
|  | Logged in users password is updated in database after submission | Submit a new password | Password for logged in user is changed | Pass
|  | User can log in with new password | Attempt to log in with new password | User can log in successfully | Pass
| **View Account Info** |  |  |  | 
|  | Account info on terminal matches account info in database | Click "view account info" | Account info matches database | Pass
|  | "Press any key to continue" operates as expected | After account info is shown, type any key. Test with multiple different keys. | Key press takes the user back to main menu | Pass on every key tested
|  | Password is hidden | View account info and look at password | Password is hidden | Pass
|  | Information for the logged in user is pulled up, not another user | Log in as SemMTM and view account info in terminal | Correct account information is shown | Pass
| **Exit** |  |  |  | 
|  | Exit message is shown and program is closed down | Select option 7 in main menu | Exit message is shown and program is closed down | Pass

## **5.2. User Tests**
3 Users were asked to create an account and use all features within the application. They were asked to provide comments on the useability of the app and any potential feedback.
| User | Features Used | User Comments | Applied Changes |
|--|--|--|--|
| User 1 | 100% | All features work well and the app is easy to use. Ability to change username would be a good feature to add. | N/A |
| User 2 | 100% | Everything works great, but the error messages could be made more noticable. | Made error message text red and success message text green |
| User 3 | 100% | Lots of cool features but having to press "back" after every action is annoying. | Changed "back" to "press any key to continue" after actions completed |

## **5.3. Validator Testing**
- Code in the run.py file has been validated using the Code Institute Python Linter: https://pep8ci.herokuapp.com/
- Results before running through validator:
  - Multiple errors in regards to visual rules (white space, long lines etc)

![Linter errors](<assets/readme images/Screenshot_37.png>)
- Results after fixing errors:

![Linter no errors](<assets/readme images/Screenshot_38.png>)