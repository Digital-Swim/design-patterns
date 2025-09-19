class Payment:

    @staticmethod
    def create(method):
        if method == "bitcoin":
            return Bitcoin()
        elif method == "stripe":
            return Stripe()
        else:
            raise ValueError("Invalid payment method")

class Stripe:

    def __init__(self):
        self.mode = "Stripe payment"
        pass
    
    def pay(self):
        print(self.mode)
    


class Bitcoin:
    def __init__(self):
        self.mode = "Bitcoin payment"
        pass
    
    def pay(self):
        print(self.mode)

    
     
payment = Payment.create("bitcoin")

payment.pay()