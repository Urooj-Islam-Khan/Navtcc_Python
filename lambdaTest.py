# --- User Data Store ---

# Usernames and passwords stored in a dictionary
users = {'user1': 'pass123'}

# Balance associated with each user
balances = {'user1': 1000}

# Empty transaction history list for each user
transactions = {'user1': []}

# --- Function Definitions ---

# Check login credentials (username and password)
check_login = lambda u, p: u in users and users[u] == p
# returns True if username exists and password matches, otherwise False

# Return the balance of the user as a formatted string
display_balance = lambda user: f"Your current balance is: ${balances[user]}"

# Deposit function using lambda
# 1. Adds amount to user's balance
# 2. Adds a deposit record in user's transaction history
deposit = lambda user, amount: (
    balances.update({user: balances[user] + amount}),
    transactions[user].append(f"Deposited: ${amount}")
)

# Withdraw function using lambda
# 1. Checks if user has enough balance
#    - If yes: subtracts amount and logs the transaction
#    - If no: prints "Insufficient funds."
withdraw = lambda user, amount: (
    (balances.update({user: balances[user] - amount}),
     transactions[user].append(f"Withdrew: ${amount}"))
    if balances[user] >= amount else
    print("Insufficient funds.")
)

# View transaction history for a user
# - Joins transaction messages with newline, or shows default message
view_history = lambda user: "\n".join(transactions[user]) if transactions[user] else "No transactions yet."


# --- ATM Menu Function ---

def atm_menu(user):
    while True:  # Infinite loop to keep showing menu until user exits
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transaction History")
        print("5. Exit")

        choice = input("Select an option (1-5): ")  # Take user input

        if choice == '1':
            # Show current balance
            print(display_balance(user))

        elif choice == '2':
            # Deposit flow
            try:
                amount = float(input("Enter amount to deposit: "))  # Get amount as float
                deposit(user, amount)  # Call deposit function
                print("Deposit successful.")
            except ValueError:
                print("Invalid amount.")  # Handle non-numeric input

        elif choice == '3':
            # Withdraw flow
            try:
                amount = float(input("Enter amount to withdraw: "))  # Get amount as float
                withdraw(user, amount)  # Call withdraw function
            except ValueError:
                print("Invalid amount.")  # Handle non-numeric input

        elif choice == '4':
            # Show transaction history
            print("Transaction History:")
            print(view_history(user))

        elif choice == '5':
            # Exit the ATM menu
            print("Thank you for using the ATM. Goodbye!")
            break  # Exit the loop

        else:
            # If user enters anything other than 1–5
            print("Invalid option. Please choose 1-5.")


# --- Main Function ---

def main():
    print("=== Welcome to the ATM System ===")
    
    # Take login input from the user
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Check credentials using lambda function
    if check_login(username, password):
        print("Login successful!")
        atm_menu(username)  # Call ATM menu if login is successful
    else:
        print("Invalid username or password.")  # Show error if login fails


# --- Start the Program ---
main()
