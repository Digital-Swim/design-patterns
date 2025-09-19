class Ticket:
    def process(self):
        print("processing ticket")
    
    def upgradeLevel(self):
        pass
    
    def downgradeLevel(self):
        pass

class Level1Ticket(Ticket):
    
    def process(self):
        print("processing tciker level1")
    
    def upgradeLevel(self)-> Ticket:
        return Level2Ticket()
    
    def downgradeLevel(self):
        return self
    
class Level2Ticket(Ticket):
  
    def process(self):
        print("processing tciker level2")
    
    def upgradeLevel(self):
        return self
    
    def downgradeLevel(self)-> Ticket:
        return Level1Ticket()
    

