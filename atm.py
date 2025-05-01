print("----------------------------------")
print("Welcome to ATM System")
print("----------------------------------")

users = {'urooj': '124', 'zainab': '12345'}

username = input("Enter your username: ")
password = input("Enter your password: ")

check_login = lambda u, p: u in users and users[u] == p

ATM = []

check_balance = lambda bill: print("Your Current Balance is: Rs", bill,".00")
deposit_money = lambda bill, amount: bill + amount
withdraw_money = lambda bill, amount: bill - amount if amount <= bill else None

def atm_menu(user):
    while True:
        bank_balance= 1000        
        print("""
1. Check your Bank Balance.
2. Deposit Money.
3. Withdraw Money.
4. View Transaction History.
5. Exit.      
""")
        try:
            option = int(input("Select an option: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if option == 1:
            check_balance(bank_balance)

        elif option == 2:
            try:
                deposit_amount = int(input("Enter your Deposit Amount: "))
                bank_balance = deposit_money(bank_balance, deposit_amount)
                ATM.append(f"Deposited Rs {deposit_amount}")
                print("Successfully deposited Rs", deposit_amount, ".00")
            except ValueError:
                print("Invalid amount!")

        elif option == 3:
            try:
                withdraw_amount = int(input("Enter amount to withdraw: "))
                if withdraw_money(bank_balance, withdraw_amount) is None:
                    print("You do not have that much amount in your account!")
                else:
                    bank_balance = withdraw_money(bank_balance, withdraw_amount)
                    ATM.append(f"Withdrawn Rs {withdraw_amount}")
                    print("Successfully withdrew Rs", withdraw_amount, ".00")
            except ValueError:
                print("Invalid amount!")

        elif option == 4:
            print("Transaction History:")
            for t in ATM:
                print(t)
            print("Now Your Total Bank Amount is: Rs", bank_balance, ".00")

        elif option == 5:
            print("Thank you for using our ATM system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Authentication check
if check_login(username, password):
    print("----------------------------------")
    print("Login Successful!!!")
    print("----------------------------------")
    atm_menu(username)
else:
    print("Invalid username or password.")
