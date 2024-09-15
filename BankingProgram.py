#Banking Program

def showBalance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an ammount to be deposited: "))

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
    else:
        return amount

def main():
    balance = 0
    isRunning = True

    while isRunning:
        print("Banking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. withdraw")
        print("4. Exit")

        print()
        choice = input("Enter your choice(1-4): ")

        if choice == "1":
            showBalance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            isRunning = False
        else:
            print("That is not a valid option")
    print("Thank you! Have a nice day!")

if __name__ == "__main__":
 main()