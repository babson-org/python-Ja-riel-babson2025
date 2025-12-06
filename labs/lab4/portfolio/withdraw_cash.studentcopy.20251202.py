
import time
def portfolio_withdraw_cash(self, amount: float):
    if amount < 0:
        print("You cannot withdraw a negative amount.")
        time.sleep(1)

    elif amount > self.cash:
        print(f"You only have ${self.cash: float}. Sell some stock first!")
        time.sleep(1)

    else:
        self.cash -= amount
        print(f"Your check for ${amount:,float} is in the mail.")
        time.sleep(1)

    return None