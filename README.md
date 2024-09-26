# ***Bank Of Sem***
![Welcome](<assets/readme images/Screenshot_36.png>)
---
## **A Terminal Based Banking Application**
A terminal based banking application that is connected to a database via API and updates the information based on user action. To use the application, a user must create an account with a unique username & 4 digit password, these are then pushed to the data base. To log in, the user must use the correct & matching credentials or access to the account will be denied.

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

#### [LIVE SITE](https://bank-of-sem-cd1ad5a802b4.herokuapp.com)
Here is the [googlesheet link](https://docs.google.com/spreadsheets/d/1DUad-T36YiIOkYjsPI-yY75BABECObcZSVzKC5_VO6M/edit?usp=sharing) so you can see what changes are being made per user action.
#### [REPOSITORY](https://github.com/SemMTM/bank_of_sem)

Please use the following log in details to use the app:
- Username: User2
- Password: 9999

List of other users to test transfer feature:
- SemMTM
- User3
- User4

---

## **Table of Contents**
1. UX
2. Features
3. Future Features
4. Technology Used 
5. Testing
6. Bugs
7. Credits
8. Deployment

# **1. Pre-project Planning**
The plan for this project was to create a terminal based banking application that would manipulate data stored in a database. All users would have unique usernames and passwords that could be changed by the user. I wanted to imitate a real banking applications features as much as possible. Every action should cause some change in the database. 

The pre planned features were:
1. Change password
2. See balance
3. Withdraw/Deposit funds
4. Send money to another user in the database
5. The ability to see a history of all actions taken on the account

### **1.2. UX Design**
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

### **1.3. User Stories**
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

### **1.4. Flow Charts**
![Flow chart](<assets/readme images/Screenshot_40.png>)

---

# **2. Features**
## **Main Menu**
- Welcomes the user to the Bank Of Sem and introduces the 2 main options.
- Prompts the user to make a selection.

![Main menu](<assets/readme images/Screenshot_2.png>)

- Throws an error if an invalid option is selected.

![Wrror message](<assets/readme images/Screenshot_1.png>)

## Create Account
**Username**
- Allows the user to create an account that will be pushed to the database. Each username must be unique or an error will be thrown.

![Enter username screen](<assets/readme images/Screenshot_4.png>)

**Password**
- Once a unique username has been selected, the user will be promted to input a 4 digit password.
- The password must be 4 numbers or an error will be thrown.
- Password input is hidden

![Enter password error message](<assets/readme images/Screenshot_5.png>)

**Account Type**
- After a valid password has been chosen, the user will be prompted to select an account type.
- Each account may only be 1 account type. Certain account types have different benefit & restrictions.
- Current accounts function like a regular bank account and have no restrictions.
- Growth accounts have a £15,000 deposit limit, can't be sent money and gain 1% interest on every log in. This interest is pushed to the database after it is calculated.

![Account type selection](<assets/readme images/Screenshot_6.png>)

**Account creation in database**
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

## **Log In**
- To log in, the details provided must match the details in the database or access will be denied.
- Usernames and passwords are paired and if the entered details do not match a pair, then an error will be thrown.
- Passwords are masked.

![Incorrect log in details](<assets/readme images/Screenshot_11.png>)

- Once the correct details are entered, the user will be shown a "loading account..." message and be taken to a main menu.

![Log in details in spreadsheet](<assets/readme images/Screenshot_14.png>)

![Correct log in details](<assets/readme images/Screenshot_12.png>)

## **Main Menu**
- The main menu shows the user all of the actions that can be taken on their account.
- If an invalid option is selected, then an error message is thrown.

![Main Menu](<assets/readme images/Screenshot_13.png>)

## **Show Balance**
- This option extracts the logged in users balance from the list of users in the spreadsheet and displays it in the terminal.

![User balance in speadsheet](<assets/readme images/Screenshot_14.png>)

![User balance in terminal](<assets/readme images/Screenshot_15.png>)

## **Withdraw/Deposit Funds**
- A user is able to withdraw/deposit funds from their account.
- The user is also shown their available balance.

![Withdraw/deposit funds menu](<assets/readme images/Screenshot_33.png>)

**Deposit funds**
- The amount a user can deposit depends on their account type.
- A current account has an unlimited deposit limit.
- A growth account has a max deposit of £15,000.

![Deposit limit for growth accounts](<assets/readme images/Screenshot_17.png>)

- Upon a successful deposit, a message with the new account balance will be displayed to the user and the amount will be added to the balance on the spreadsheet.
- If the account is a growth account then a message telling them their remaining deposit amount of their £15,000 limit.

![successful deposit](<assets/readme images/Screenshot_19.png>)

![spreadsheet updated with deposit amount](<assets/readme images/Screenshot_20.png>)

**Withdraw funds**
- The user can't withdraw more money then they have in their account.

![insufficient funds for withdrawl message](<assets/readme images/Screenshot_18.png>)

- The user is prompted with the amount they would like to withdraw. After a valid amount has been specified, the withdraw amount is taken 
    away from their balance.
- After a successful withdrawl, the user is shown a message with their new balance and the spreadsheet is updated.

![Successful withdrawl](<assets/readme images/Screenshot_21.png>)

![Successful withdrawl update in spreadsheet](<assets/readme images/Screenshot_22.png>)

## **Send Money To Another User**
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

## **See Account History**
- Every action on a logged in users account is saved and time stamped in the users "history" tab.
- These actions are pushed to the database and can be called & displayed in the terminal.
- The data has been formatted to be more readable for the user.

![View account history in terminal](<assets/readme images/Screenshot_28.png>)

![View account history in database](<assets/readme images/Screenshot_29.png>)

## **Change Password**
- The logged in user can change the password associated with their account.
- The changing password follows the same validation as creating one at log in. It must be 4 numbers only and will throw an error if not.

![Change password error](<assets/readme images/Screenshot_30.png>)

- After the new password is created, the database will be updated and the user must use this new password to log in to their account in the future.

![Change password updated](<assets/readme images/Screenshot_31.png>)

![Change password updated in database](<assets/readme images/Screenshot_32.png>)

## **View Account Info**
- This feature works similarly to the "See Acount History" feature.
- It allows the logged in user to see all of their key account information.
- The data has been formatted to be more readable for the user and the password is hidden.

![View account info](<assets/readme images/Screenshot_34.png>)

![View account info](<assets/readme images/Screenshot_35.png>)

---

# **3. Future Features**
- Hash passwords for further security.
- Add interest daily on growth accounts rather then per log in.
- Ability to log in via email and recieve account information directly to email address.
- A front end GUI instead of a terminal based UI.
- See all transactions
- See account history by filter option

---

# **4. Technology Used**
### **Languages**
- Python

### **Frameworks, Libraries, Programs Used & APIs**
- Git:
  - Used for version control by utilising VSCode terminal to commit to Git and push to GitHub.
- GitHub: 
  - Used to store the projects code after being pushed from Git.
- Heroku: 
  - Used to deploy the project in a mock terminal so users can interact with the project.
- Google Cloud Services: 
  - Used to generate API credentials so the program can access the database.
- Gspread Library:
  - A library used to manipulate the google sheet.
- Google Drive: 
  - Used to store the google sheet used by the application.
- Google Sheets API: 
  - Used to read and write Google Sheets data.
- Google Drive API: 
  - Used to create and manage the bank of sem spreadsheet.
- Google Auth
  - Uses the creds.json file to set up authentication needed to access the google cloud project.
- Nodejs
  - Used to handle the mock terminal code provided by Code Institute in the project template.
- Colorama Module
  - Used to colour success and error messages for better user experience.
- PWInput Module
  - Used to mask password inputs.

---

# **5. Testing**
For all testing please refer to the [TESTING](TESTING.md) file.

---

# **6. Bugs**
### **6.1. Fixed Bugs**
Throughout testing, multiple bugs were discovered. All discovered bugs were fixed and documented below.

| Bug | Solution |
|--|--|
| When entering anything other then a number in "Deposit Amount", a ValueError is thrown | Used a while True loop to loop the input if an invalid answer is given. Used a Try, Except statement to handle the error if input cannot be converted to an integer |
| When entering anything other then a number in "Withdraw Amount", a ValueError is thrown | Used a while True loop to loop the input if an invalid answer is given. Used a Try, Except statement to handle the error if input cannot be converted to an integer |
| When entering anything other then a number in "Transfer Amount", a ValueError is thrown | Used a while True loop to loop the input if an invalid answer is given. Used a Try, Except statement to handle the error if input cannot be converted to an integer |
| User can enter negative amount in "Send Money" function and can reduce another users balance while increasing their own | Added "if int(amount_to_send) < 0:" to elif statment for validation of input |

### **6.2. Unfixed Bugs**
There are no known unfixed bugs as of 25.09.2024.

---

# **7. Credits**

### **7.1. Content & Resources**
- How to use any() to check if an element exists in a list: https://www.analyticsvidhya.com/blog/2024/02/check-if-element-exists-in-list-in-python/#:~:text=Using%20the%20%27any()%27%20Function,-The%20%27any()&text=You%20can%20determine%20if%20it,"Element%20not%20found."%20
- Used validate_data function from the Love Sandwiches project
- How to populate the next empty cell in a col with a specifed value: https://stackoverflow.com/questions/40781295/how-to-find-the-first-empty-row-of-a-google-spread-sheet-using-python-gspread
- How to generate a random number of digits: https://stackoverflow.com/questions/2673385/how-to-generate-a-random-number-with-a-specific-amount-of-digits
- How to verify if the input can be converted into an integer: https://stackoverflow.com/questions/56202563/how-can-i-restart-a-function-if-the-argument-isnt-numeric
- Help with use on classes: https://realpython.com/python-classes/#:~:text=Encapsulate%20related%20data%20and%20behaviors,even%20reuse%20across%20multiple%20projects

### **7.2 Acknowledgements**
- I would like to thank my Code Institute mentor Gareth Mc Girr for providing valuable feedback and great suggestions that helped me greatly improve this project.

---

# **8. Deployemnt**
As this project was entirely Python & terminal based, it was deployed on [Heroku](https://id.heroku.com/login) which enables deployments of dynamic websites that don't use just front-end languages. The deployed project uses a mock terminal so that users can interact with it through a web browser. This was set up by the Code Institute Engineering team in the template used for this project; which provided the files and code needed to properly deploy the project on Heroku.

[Bank of Sem Live Site](https://bank-of-sem-cd1ad5a802b4.herokuapp.com)

The steps taken to deploy this project are as follows:
1. Create a list of dependencies for the project to run properly on Heroku. To do this:
    1. Create a blank requirements.txt file
    2. Open the file and in the terminal type "pip3 freeze > requirements.txt"
    3. The file name must be exactly the same as Heroku searches for this file during deployment
    4. The file will be updated with all necessary dependencies
2. Create an account on [Heroku](https://id.heroku.com/login)
3. Add billing information and purchase platform credits
4. On the dashboard click "Create new app"
5. Name the app and select a location, each app name on Heroku needs to be unique
6. Click "Create app"
7. Once in your app dashboard, click on the "Settings" tab. It is important to get the settings set up before attemping to deploy the app
8. Set up app settings. To do this:
    1. Navigate to the "Config Vars" section and click "Reveal config vars"
    2. In the "KEY" field, enter "CREDS" in all capital letters
    3. Go to your Github project and navigate to your creds.json file and copy its contents
    4. In the "VALUE" field, paste your entire creds.json file contents and click "add"
9. Navigate to the "Buildpacks" section and click "Add buildpack"
    - Add the Python buildpack and the Nodejs buildpack
    - The Pyhton buildpack must be above the Nodejs buildpack
10. Navigate to the "Deploy" tab and select "GitHub"
11. Click "Connect to Github" and log in to your GitHub account
12. Search for your GitHub repository in the "Connect to GitHub section"
13. Once found click "connect" then click "Enable Automatic Deploy
    - Automatic deploy will redploy your project eveytime new changes are pushed to GitHub
14. Once deployment is complete, click "View" to see your deployed project

### Cloning
To clone this Repository:
1. Go to the [repository](https://github.com/SemMTM/bank_of_sem)
2. Click the "Code" button above the list of files
3. Select how you would prefer to clone the repo, using HTTPS, SSH or GitHub CLI
4. Click the "Copy" button to copy the URL to your clipboard
5. Open Git Bash or Terminal
6. Change the current working directory to where you want the cloned directory 
7. In your IDE Terminal, type the following command to clone the repository 
