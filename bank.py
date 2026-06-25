import json
import os


FILE = "accounts.json"


# Create file if not exists
if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)



# Load accounts

def load_accounts():

    with open(FILE,"r") as f:
        return json.load(f)



# Save accounts

def save_accounts(accounts):

    with open(FILE,"w") as f:
        json.dump(accounts,f,indent=4)



# Create Account

def create_account():

    accounts = load_accounts()

    acc_no = input("Enter Account Number: ")

    if acc_no in accounts:
        print("Account already exists")

    else:

        name = input("Enter Name: ")

        balance = float(input("Enter Initial Deposit: "))


        accounts[acc_no] = {

            "name":name,
            "balance":balance

        }


        save_accounts(accounts)

        print("Account Created Successfully")



# Deposit Money

def deposit():

    accounts = load_accounts()

    acc_no=input("Account Number: ")


    if acc_no in accounts:

        amount=float(input("Deposit Amount: "))


        accounts[acc_no]["balance"] += amount


        save_accounts(accounts)


        print("Money Deposited")


    else:

        print("Account not found")



# Withdraw Money

def withdraw():

    accounts=load_accounts()

    acc_no=input("Account Number: ")


    if acc_no in accounts:


        amount=float(input("Withdraw Amount: "))


        if accounts[acc_no]["balance"] >= amount:


            accounts[acc_no]["balance"] -= amount


            save_accounts(accounts)


            print("Withdrawal Successful")


        else:

            print("Insufficient Balance")


    else:

        print("Account not found")




# Check Balance

def check_balance():

    accounts=load_accounts()


    acc_no=input("Account Number: ")


    if acc_no in accounts:

        print("Name:",accounts[acc_no]["name"])

        print("Balance:",accounts[acc_no]["balance"])


    else:

        print("Account not found")




# Main Menu

while True:


    print("""
    ===== BANKING SYSTEM =====

    1. Create Account

    2. Deposit Money

    3. Withdraw Money

    4. Check Balance

    5. Exit

    """)


    choice=input("Enter Choice: ")



    if choice=="1":

        create_account()


    elif choice=="2":

        deposit()


    elif choice=="3":

        withdraw()


    elif choice=="4":

        check_balance()


    elif choice=="5":

        print("Thank You")

        break


    else:

        print("Invalid Choice")
