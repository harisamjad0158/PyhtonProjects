class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount:.2f} successfully.")
        else:
            print("Invalid amount for deposit. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount:.2f} successfully.")
        else:
            print("Insufficient funds or invalid amount for withdrawal.")

    def get_balance(self):
        return self.balance


def main():
    account_holder_name = input("Enter the account holder's name: ")
    initial_balance = float(input("Enter the initial balance: "))

    # Create a bank account object
    account = BankAccount(account_holder_name, initial_balance)

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = int(input("Enter your choice (1/2/3/4): "))

        if choice == 1:
            deposit_amount = float(input("Enter the amount to deposit: "))
            account.deposit(deposit_amount)

        elif choice == 2:
            withdraw_amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(withdraw_amount)

        elif choice == 3:
            print(f"Your current balance is: {account.get_balance():.2f}")

        elif choice == 4:
            print("Thank you for using our Bank!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()