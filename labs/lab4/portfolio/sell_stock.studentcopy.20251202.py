
import time
import prices as _prices


def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_sell_stock(self, sym: str, shares: float, price: float):

    # ---- Ensure symbol exists ----------------------------------------------
    pos = _find_position(self, sym)
    if not pos:
        print(f"Position for {sym} not found.")
        return

    # ---- Ensure number of shares is valid -----------------------------------
    if shares <= 0:
        print("Shares must be positive.")
        return

    if shares > pos["shares"]:
        print(f"Insufficient shares to sell {shares} of {sym}.")
        return

    # ---- Get latest market price -------------------------------------------
    last_close_map = _prices.get_last_close_map([sym])
    if sym not in last_close_map:
        print(f"Price data unavailable for {sym}")
        return

    market_price = last_close_map[sym]
    proceeds = market_price * shares

    # ---- Adjust position using proportional cost accounting -----------------
    # cost_per_share = total cost / total shares
    cost_per_share = pos["cost"] / pos["shares"] 
    if pos["shares"] > 0: 
    cost_reduction = cost_per_share * shares

    # Update position
    pos["shares"] -= shares
    pos["cost"] -= cost_reduction

    # ---- Remove position if all shares sold --------------------------------
    if pos["shares"] == 0:
        self.positions.remove(pos)

    # ---- Add proceeds to cash ----------------------------------------------
    self.cash += proceeds

    return
