user_info = {
    "name": "Girisha",
    "pin": "2200",
    "balance": 50000
}
print("WELCOME TO ATM")
attempts = 3
while attempts > 0:
    pin = input("Enter ATM PIN: ")
    if pin == user_info["pin"]:
        print("PIN is Correct")
        print("""
1. Withdraw
2. Deposit
3. Check Balance
4. Exit
""")
        choice = int(input("Enter your choice: "))
        # Withdraw
        if choice == 1:
            amt = int(input("Enter amount: "))
            if amt <= user_info["balance"]:
                user_info["balance"] = user_info["balance"] - amt
                print("Collect Cash")
                print("Remaining Balance:", user_info["balance"])
            else:
                print("Insufficient Balance")
        # Deposit
        elif choice == 2:
            amt = int(input("Enter amount: "))
            user_info["balance"] = user_info["balance"] + amt
            print("Amount Deposited")
            print("Updated Balance:", user_info["balance"])
        # Check Balance
        elif choice == 3:
            print("Your Balance is:", user_info["balance"])
        # Exit
        elif choice == 4:
            print("Thank You")
        else:
            print("Invalid Choice")
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print(f"Wrong PIN | Attempts Left: {attempts}")
        else:
            print("CARD BLOCKED")
