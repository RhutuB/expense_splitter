# logic.py

def calculate_balances(expenses, people):
    total = sum(expenses.values())
    share = total / len(people)

    balances = {
        person: expenses.get(person, 0) - share
        for person in people
    }

    return balances, total, share


def settle_expenses(balances):
    debtors = []
    creditors = []

    for person, amount in balances.items():
        if amount < 0:
            debtors.append([person, -amount])
        elif amount > 0:
            creditors.append([person, amount])

    debtors.sort(key=lambda x: x[1])
    creditors.sort(key=lambda x: x[1])

    settlements = []
    i = j = 0

    while i < len(debtors) and j < len(creditors):
        debtor, owes = debtors[i]
        creditor, gets = creditors[j]

        amt = min(owes, gets)

        settlements.append(f"{debtor} pays ₹{amt:.2f} to {creditor}")

        debtors[i][1] -= amt
        creditors[j][1] -= amt

        if debtors[i][1] == 0:
            i += 1
        if creditors[j][1] == 0:
            j += 1

    return settlements
