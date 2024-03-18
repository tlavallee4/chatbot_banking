"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: {Student Name}
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:
## get account with empty parentheses - not taking any parameters
## prompt user to enter their account number
def get_account():
    account_number = input("Please enter your account number: ")

## attempting to return account number as an integer
## raises exceptions if the number entered is not a whole number or does not exist in the ACCOUNTS dictionary
    try:
        account_number = int(account_number)
    except ValueError:
        raise ValueError("Account number must be a whole number.")
    if account_number not in ACCOUNTS:
        raise ValueError("Account number entered does not exist.")
    
    return account_number

# get amount with empty parentheses - not taking any parameters
# prompt user to enter their amount
def get_amount():
    account_amount = input("Enter the transaction amount:")
    #returning account number as float
    #raises exceptions if the amount entered is not numeric or is negative
    try:
        account_amount = float(account_amount)
    except ValueError:
        raise ValueError("Invalid amount. Amount must be numeric.")
    if account_amount <= 0:
        raise ValueError("Invalid amount. Please enter a positive number.")
    return account_amount

# getting the account balance from ACCOUNTS dictionary
def get_balance(account: int):   
    if account in ACCOUNTS:
        balance = ACCOUNTS[account]['balance']
        return f"Your current balance for account {account} is ${balance:.2f}."
    # raising ValueError if account number does not exist in the ACCOUNTS dictionary
    else:
        raise ValueError("Account number does not exist.")

# Making a deposit
# raises ValueErrors if the account number is less than 0 or does not exist
def make_deposit(account: int, amount: float):
    if account not in ACCOUNTS:
        raise ValueError("Account number does not exist.")
    elif amount < 0:
        raise ValueError("Invalid Amount. Amount must be positive.")
    # retrieving the value of the balance from the accounts dictionary
    # adding the deposit amount and updating the new accounts dictionary
    else:
        balance = ACCOUNTS[account]['balance']
        new_balance = balance + amount
    
    return f"Your current balance for account {account} is ${new_balance:.2f}."

# prompting user for selection
def user_selection():
    selected_task = input("What would you like to do (balance/deposit/exit)?")
    selected_task = selected_task.lower()
    # raise ValueError if task is invlad
    if selected_task not in VALID_TASKS:
        raise ValueError("Invalid task. Please choose balance, deposit, or exit.")
    
    return selected_task





        
        
        

    
        


## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:


            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:


                        valid_account = True
                    except ValueError as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except ValueError as e:
                            # Invalid amount.
                            print(e)
                ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                ## VARIABLES account AND amount DEFINED ABOVE AND 
                ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except ValueError as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""