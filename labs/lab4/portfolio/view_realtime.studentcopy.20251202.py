
import prices as _prices

def portfolio_view_realtime(self):
    # Extract tickers from positions
    syms = [pos["sym"] for pos in self.positions]

    # Fetch realtime prices
    px_map = _prices.get_live_map(syms)

    return px_map