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
|  | The "Back" option operates as expected | After balance is shown, select option 1. | The "Back" option takes the user back to main menu | Pass
|  | Error thrown when user option != 1 in back menu selection | Enter number 2 | Error message is thrown and user is prompted to reselect an option | Pass
| **Withdraw/Deposit Funds** |  |  |  | 
|  | Users balance is displayed above menu selection | Check the balance shown against users detail in the spreadsheet matches balance displayed | Both balances match (in the spreadsheet and shown above menu) | Pass
|  | User is promted to add deposit amount | Press option 1. in the sub-menu | User is promted to add deposit amount | Pass
|  | Users can add funds to their balance | Add a deposit amount of 500 | Balance is incremented by 500 | Pass
|  | New balance is pushed to spreadsheet | Add a deposit amount of 500 | Users balance on spreadsheet matches new balance specified in terminal after deposit | Pass
|  | A user cannot deposit more than 25000 per transaction | Add a deposit amount of 30000 | Error message is thrown and user is prompted to re-enter an amount | Pass
|  | A growth account cannot be deposited more than their £15,000 limit | Log in with a growth account, deposit more then their remaining available limit | Error message is thrown and user is prompted to re-enter an amount | Pass
| **Send Money** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **See Account History** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **Change Password** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **View Account Info** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **Exit** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## **5.2. Peer Code Review**

## **5.3. User Tests**

## **5.4. Validator Testing**