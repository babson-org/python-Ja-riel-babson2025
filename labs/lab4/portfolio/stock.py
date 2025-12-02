
class Stock:
    def __init__(self, sym, name, shares=0.0, cost=0.0):
        """TODO:"""
        
        
       

    def __str__(self):
        """TODO: include symbol, shares, and cost (format flexible)."""
        
        return f"COMPLETE THIS LINE"
        





class Stock:
    def __init__(self, sym, name, shares=0.0, cost=0.0):
        """TODO:
        - Save symbol, name, shares, and cost into object attributes
        """
        self.sym = sym
        self.name = name
        self.shares = float(shares)
        self.cost = float(cost)

    def __str__(self):
        """TODO: include symbol, shares, and cost (format flexible)."""
        return f"{self.sym}: shares={self.shares}, cost=${self.cost:.2f}"