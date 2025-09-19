
from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def onEvent(self, event):pass

class Trader(Observer):
    def __init__(self, name):
        self.name = name
    
    def onEvent(self, event):
        print(f" {self.name}: {event} ")
    
class Stock:
    def __init__(self, name):
        self.name = name
        self.observers:list[Observer] = []
        pass
    
    def attach(self, observer:Observer):
        self.observers.append(observer)

    def notify(self, event:str):
        for observer in self.observers:
            observer.onEvent(self.name+ "_" + event)
    
    def up(self):
        print(f"stock {self.name} is up")
        self.notify("Up")

stock = Stock("Google")

trader1 = Trader("Ranjit")
trader2 = Trader("Jas")


stock.attach(trader1)
stock.attach(trader2)

stock.up()