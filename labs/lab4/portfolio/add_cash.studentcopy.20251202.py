import time
def portfolio_add_cash(self, amount: float):
    if amount < 0:
        print("Cannot add a negative amount of cash.")
        return
    elif amount == 0:
        print("No cash added.")
        return
    else:
        self.cash += amount
        print(f"Added ${amount} to cash. New cash balance: ${self.cash: float}.")