class ATM:
    def __init__(self, name, aadhaar, mobile, acc_no, pin, balance):
        self.name = name
        self.aadhaar = aadhaar
        self.mobile = mobile
        self.acc_no = acc_no
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def withdraw(self):
        amt = int(input("Enter Amount to Withdraw: "))

        if amt <= self.balance:
            self.balance -= amt
            self.transactions.append(f"Withdraw: ₹{amt}")
            print("Please Collect Your Cash")
            print("Remaining Balance:", self.balance)
        else:
            print("Insufficient Balance")

    def deposit(self):
        amt = int(input("Enter Amount to Deposit: "))
        self.balance += amt
        self.transactions.append(f"Deposit: ₹{amt}")
        print("Amount Deposited Successfully")
        print("Updated Balance:", self.balance)

    def check_balance(self):
        print("Available Balance: ₹", self.balance)

    def profile(self):
        print("\n----- ACCOUNT DETAILS -----")
        print("Name          :", self.name)
        print("Aadhaar No    :", self.aadhaar)
        print("Mobile No     :", self.mobile)
        print("Account No    :", self.acc_no)
        print("Balance       : ₹", self.balance)

    def mini_statement(self):
        print("\n----- MINI STATEMENT -----")
        if self.transactions:
            for t in self.transactions:
                print(t)
        else:
            print("No Transactions Yet")

    def menu(self):
        while True:
            print("""
======== ATM MENU ========

1. Withdraw
2. Deposit
3. Check Balance
4. Profile Details
5. Mini Statement
6. Exit

==========================
""")

            choice = int(input("Enter Choice: "))

            if choice == 1:
                self.withdraw()

            elif choice == 2:
                self.deposit()

            elif choice == 3:
                self.check_balance()

            elif choice == 4:
                self.profile()

            elif choice == 5:
                self.mini_statement()

            elif choice == 6:
                print("Thank You For Banking With Us")
                break

            else:
                print("Invalid Choice")

    def login(self):
        attempts = 3

        while attempts > 0:
            entered_pin = input("Enter ATM PIN: ")

            if entered_pin == self.pin:
                print("\nLogin Successful")
                self.menu()
                return

            else:
                attempts -= 1

                if attempts > 0:
                    print("Wrong PIN | Attempts Left:", attempts)

                else:
                    print("CARD BLOCKED")


# Object Creation
user = ATM(
    "Thangavalu Girisha",
    "1234 5678 9012",
    "9014679299",
    "567890123456",
    "1219",
    50000
)

print("===== WELCOME TO UNION ATM =====")
user.login()
