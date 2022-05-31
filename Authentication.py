# To Register
# - first name, last name, password, email address
# - generate user account


# to login
# account number and password


# bank operations 


import random

data_base = {}

def init():                                 #this is initializing the system hence a point of entry
    is_option_valid = False
    print("Welcome to BB Bank!")

    while is_option_valid == False:

        have_account = int(input("Do you have an account with us: 1(yes) 2(no) \n"))
    
        if (have_account == 1):
            is_option_valid = True
            login()

        elif (have_account == 2):
            is_option_valid = True
            print(register())
        else:
            print("You have made an invalid entry.")


    
def login():            #defining the login function
        print("************ Login ************")

        correct_login_info = False

        while correct_login_info == False:

            account_holder_id = int(input("Enter your account number. \n"))
            your_password = input("Enter your password.\n")

            for account_number, password in data_base.items[3]:
                if(account_number == account_holder_id):
                    if(password == your_password):
                        correct_login_info = True

            print("Incorrect account number or password entered.")

        bank_operation()


def register():                             #defining the register function
    print("***** Register *****")

    email = input("Enter your Email address. \n")
    first_name = input("Enter your first name. \n")
    last_name = input("Enter your surname. \n")
    password = input("Enter a password. \n")

    account_number = generate_account_number()

    data_base[account_number] = [first_name, last_name, email, password]
   

    print("You account has been created.")
    print("************    *************")
    print("Your account number is: %d" % account_number)
    print("************    *************")
    print ("Make sure you keep it safe")
    print("************    *************")

    login()

def bank_operation():                                   #defining the bank operation function
    select_option = input("what do you want to do today?: 1(Withdrawal) 2(Deposit) 3(Logout) 4(Exit)\n")

    if (select_option == 1):
        withdrawal_operations()

    elif(select_option == 2):
        deposit_operations()

    elif(select_option == 3):
        login()
    
    elif(select_option == 4):
        exit() 

    else:
        print("Invalid operation selected")
        bank_operation()
 
def withdrawal_operations():
    print("How much do you want to withdraw?")

def deposit_operations():
    print("How much do you want to deposit?")

def generate_account_number():
    # print("Please wait your account number is being generated")
    return random.randrange(1111111111,9999999999)
    
    #### ACTUAL BANKING SYSTEM ####

#print(generate_account_number())
init()
