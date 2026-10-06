# ====================================================
# Assignment: ATM Card Mechanism Using Basic Python
# ====================================================

# Customer Database (In-memory storage)
accounts = {
    "1234": {"name": "Rahul", "pin": "1234", "balance": 25000.0},
    "5678": {"name": "Priya", "pin": "5678", "balance": 40000.0},
    "9012": {"name": "Amit", "pin": "4321", "balance": 15000.0},
    "3456": {"name": "Sneha", "pin": "1122", "balance": 50000.0},
    "7890": {"name": "Rohan", "pin": "9988", "balance": 18000.0},
}

# Main Application Loop (System Level)
while True:
    print("\n" + "=" * 40)
    print("           WELCOME TO THE ATM           ")
    print("=" * 40)
    print("(Type 'exit' to shut down the ATM system)")
    card_input = input("Enter your ATM card number: ").strip()

    # System Quit (Terminates the entire application)
    if card_input.lower() in ["exit", "quit"]:
        print("\nShutting down ATM system. Have a great day!")
        break

    # 1. Card Validation
    if card_input not in accounts:
        print("Invalid card number. Access denied.")
        continue

    user = accounts[card_input]

    # 2. Initial Login Authentication
    pin_input = input("Enter your PIN: ").strip()
    if pin_input != user["pin"]:
        print("Incorrect PIN. Access denied.")
        continue

    print(f"\nAuthentication successful.\nWelcome {user['name']}!")

    # 3. Account-Level Session Loop
    while True:
        print("\n" + "=" * 25)
        print("        ATM MENU        ")
        print("=" * 25)
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Exit (Collect Card)")
        print("=" * 25)

        choice = input("Enter your choice: ").strip()

        # ----------------------------------------------------
        # Option 1: Check Balance
        # ----------------------------------------------------
        if choice == "1":
            verify_pin = input("Enter your PIN to view balance: ").strip()
            if verify_pin == user["pin"]:
                print("\n--- ACCOUNT BALANCE ---")
                print(f"Account Holder: {user['name']}")
                print(f"Available Balance: ₹{user['balance']:,.2f}")
            else:
                print("Incorrect PIN. Transaction denied.")

        # ----------------------------------------------------
        # Option 2: Withdraw Money
        # ----------------------------------------------------
        elif choice == "2":
            verify_pin = input("Enter your PIN to withdraw money: ").strip()
            if verify_pin == user["pin"]:
                amount_str = input("Enter amount to withdraw: ").strip()
                if amount_str.replace(".", "", 1).isdigit():
                    amount = float(amount_str)
                    if amount <= 0:
                        print("Error: Amount must be greater than zero.")
                    elif amount > user["balance"]:
                        print("Error: Insufficient balance.")
                    else:
                        user["balance"] -= amount
                        print(f"₹{amount:,.2f} withdrawn successfully.")
                        print(f"Remaining Balance: ₹{user['balance']:,.2f}")
                else:
                    print("Error: Invalid numerical amount.")
            else:
                print("Incorrect PIN. Transaction denied.")

        # ----------------------------------------------------
        # Option 3: Deposit Money
        # ----------------------------------------------------
        elif choice == "3":
            verify_pin = input("Enter your PIN to deposit money: ").strip()
            if verify_pin == user["pin"]:
                amount_str = input("Enter amount to deposit: ").strip()
                if amount_str.replace(".", "", 1).isdigit():
                    amount = float(amount_str)
                    if amount <= 0:
                        print("Error: Amount must be greater than zero.")
                    else:
                        user["balance"] += amount
                        print(f"₹{amount:,.2f} deposited successfully.")
                        print(f"Updated Balance: ₹{user['balance']:,.2f}")
                else:
                    print("Error: Invalid numerical amount.")
            else:
                print("Incorrect PIN. Transaction denied.")

        # ----------------------------------------------------
        # Option 4: Change PIN
        # ----------------------------------------------------
        elif choice == "4":
            current_pin = input("Enter current PIN: ").strip()
            if current_pin == user["pin"]:
                new_pin = input("Enter new PIN: ").strip()
                confirm_pin = input("Confirm new PIN: ").strip()

                if new_pin == confirm_pin:
                    if new_pin != "":
                        user["pin"] = new_pin
                        print("PIN changed successfully.")
                    else:
                        print("Error: PIN cannot be empty.")
                else:
                    print("Error: New PIN and Confirm PIN do not match.")
            else:
                print("Error: Incorrect current PIN.")

        # ----------------------------------------------------
        # Option 5: Account Quit (Return card, save session state)
        # ----------------------------------------------------
        elif choice == "5":
            print("\nThank you for using our ATM.")
            print("Please collect your card.")
            print("Have a nice day!")
            break  # Exits only this user's session back to card input

        else:
            print("Invalid choice. Please select a valid option (1-5).")
