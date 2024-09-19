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

#### Live site: 
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
The plan for this project was to create a terminal based banking application that would manipulate data stored in a database. All users would have unique usernames and pins that could be changed by the user. I wanted to imitate a real banking applications features as much as possible. Every action should cause some change in the database. 

The pre planned features were:
1. Change password
2. See balance
3. Withdraw/Deposit funds
4. Send money to another user in the database
5. The ability to see a history of all actions taken on the account

### 1.2. UX Design
As I had quite a few features planned and this was a terminial based program, the user needs a way to easily navigate back an forth between all the features. The user would select their options from a predetermined & numbered option list. Each menu after selection will have relevant sub-options. 

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

### 1.4. Flow Charts

## 2. Features

## 3. Future Features

## 4. Technology Used
### Python

### Gspread

## 5. Testing
### 5.1. General Testing 
<details>
<summary>Testing Table (Click to expand)</summary>

| What we are testing | How we test it | What we expect to happen | Result |
|--|--|--|--|
|  |  |  |  |

</details>

### 5.2. Peer Code Review

### 5.3. User Tests

### 5.4. Validator Testing

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