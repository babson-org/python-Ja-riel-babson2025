

import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    """TODO:    
    - Validate sym in DOW30
         In the lab4 folder is a file prices.py.  Look at the file and find out what DOW30 is
         You can access DOW30 with _prices.DOW30 (see how we import prices above)
    - Validate shares > 0
    - Fetch last-close price via _prices.get_last_close_map([sym]) (use this price to buy shares)
    - Make sure the client has enough cash to make the purchase (price * shares)

    - IMPORTANT: in self.positions there should only be one dictionary per symbol

    - Add the purchase to an existing position or create a new position in self.positions 
    - Be sure to decrease the client cash attribute
    NOTE: UI prompts are handled in main.py: this method only prints for invalid ticker and insufficient funds. The rest are handled in main.py
    """
    
    return




import prices as _prices
import time

def _find_position(self, sym):
    for p in self.positions:
        if p.get("sym") == sym:
            return p
    return None

def portfolio_buy_stock(self, sym: str, shares: float, price: float):
    # ---- Validate ticker ----------------------------------------------------
    if sym not in _prices.DOW30:
        print(f"Invalid ticker: {sym}")
    else:
        return

    # ---- Validate shares ----------------------------------------------------
    if shares <= 0:
        print("Shares must be positive.")
        return

    # ---- Get actual market price -------------------------------------------
    last_close_map = _prices.get_last_close_map([sym])
    if sym not in last_close_map:
        print(f"Price data unavailable for {sym}")
        return

    market_price = last_close_map[sym]
    total_cost = market_price * shares

    # ---- Check available cash ----------------------------------------------
    if self.cash < total_cost:
        print("Insufficient funds.")
        return

    # ---- Update existing position or create new -----------------------------
    pos = _find_position(self, sym)

    if pos:
        # Update existing position
        pos["shares"] += shares
        pos["cost"] += total_cost
    else:
        # Create new position dictionary
        new_pos = {
            "sym": sym,
            "name": sym,
            "shares": shares,
            "cost": total_cost
        }
        self.positions.append(new_pos)

    # ---- Deduct cash --------------------------------------------------------
    self.cash -= total_cost

    return