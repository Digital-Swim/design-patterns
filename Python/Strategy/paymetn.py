from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self):pass

class Stripe(PaymentStrategy):
    def pay(self):
        print("Stripe payment")

class Bitcoin(PaymentStrategy):
    def pay(self):
        print("Bitcoin payment")


class PaymentProcess:
    
    def __init__(self, strategy:PaymentStrategy):
        self.strategy = strategy
    
    def pay(self):
        self.strategy.pay()
    
    def set_strategy(self, strategy:PaymentStrategy):
        self.strategy = strategy

process = PaymentProcess(Stripe())
process.pay()

process.set_strategy(Bitcoin())
process.pay()    
    