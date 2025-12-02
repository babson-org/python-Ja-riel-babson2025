import prices as _prices

def portfolio_view_last_close(self):
    """
    Look at the prices.py file again.  _prices.get_last_close(symbols)
    takes a list of tickers and returns a dictionay whose keys are symbols 
    and values are last close

    create a list of tickers from positions and return the dictionary
    you get back from calling _prices.last_night_close(symbols)

    the main program does the rest!
    
    """
    



import prices as _prices

def portfolio_view_last_close(self):
    """
    - Build a list of tickers from current positions
    - Call _prices.get_last_close(symbols)
    - Return the dictionary of last-close prices
    """
    # Extract ticker symbols from positions
    symbols = [pos["sym"] for pos in self.positions]

    # If no positions, return empty dict
    if not symbols:
        return {}

    # Fetch last-close prices
    last_close = _prices.get_last_close(symbols)

    return last_close