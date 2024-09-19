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
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **Main Menu** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **Show Balance** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
| **Withdraw/Deposit Funds** |  |  |  | 
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
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