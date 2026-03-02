# main.py
from logic import calculate_balances, settle_expenses

# Colors
RED = "\033[91m"
GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def show_menu():
    print(f"\n{CYAN}--- Smart Expense Splitter ---{RESET}")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Show Summary")
    print("4. Calculate Settlements")
    print("5. Export Settlements to File")
    print("6. Exit")
    print("------------------------------")

def main():
    expenses = {}
    people = set()
    last_settlements = None

    while True:
        show_menu()
        choice = input("Enter choice: ").strip()

        if choice == "1":
            name = input("Enter name: ").strip()

            if not name:
                print(f"{RED}Name cannot be empty.{RESET}")
                continue

            try:
                amount = float(input("Amount paid: "))
                if amount < 0:
                    print(f"{RED}Amount cannot be negative.{RESET}")
                    continue

            except ValueError:
                print(f"{RED}Invalid amount. Enter a number.{RESET}")
                continue

            people.add(name)
            expenses[name] = expenses.get(name, 0) + amount
            print(f"{GREEN}Added: {name} paid ₹{amount}{RESET}")

        
        elif choice == "2":
            if not expenses:
                print(f"{RED}No expenses added yet.{RESET}")
            else:
                print("\n--- Expenses ---")
                for p, amt in expenses.items():
                    print(f"{p}: ₹{amt:.2f}")

        
        elif choice == "3":
            if not expenses:
                print(f"{RED}No expenses added yet.{RESET}")
                continue

            balances, total, share = calculate_balances(expenses, people)

            print("\n--- Summary ---")
            print(f"Total: ₹{total:.2f}")
            print(f"Per Person: ₹{share:.2f}")
            print("\nBalances:")
            for p, b in balances.items():
                color = GREEN if b > 0 else RED if b < 0 else RESET
                print(f"{color}{p}: {b:.2f}{RESET}")

        
        elif choice == "4":
            if not expenses:
                print(f"{RED}No expenses added yet.{RESET}")
                continue

            balances, _, _ = calculate_balances(expenses, people)
            last_settlements = settle_expenses(balances)

            print("\n--- Settlements ---")
            if last_settlements:
                for s in last_settlements:
                    print(s)
            else:
                print(f"{GREEN}All settled already.{RESET}")

        
        elif choice == "5":
            if not last_settlements:
                print(f"{RED}Run settlements first (option 4).{RESET}")
                continue

            with open("settlements.txt", "w", encoding="utf-8") as f:
                for line in last_settlements:
                    f.write(line + "\n")

            print(f"{GREEN}Saved to settlements.txt{RESET}")

       
        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print(f"{RED}Invalid choice. Try again.{RESET}")


if __name__ == "__main__":
    main()

