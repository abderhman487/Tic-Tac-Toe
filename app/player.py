class Player:
    def __init__(self, name, symbol):
        self.name = ""
        self.symbol = ""
    
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")
            if name.isalpha():
                self.name = name
                break
            print("Invalid name! \nPlease use letters only")
    
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (x or o): ")        
            if symbol.isalpha() and len(symbol)==1 and (symbol.upper()=="X" or symbol.upper=="O"):
                self.symbol = symbol.upper()
                break
            print ("Invalid symbol! \nPlease enter X or O")
            


