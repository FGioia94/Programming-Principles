class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def process(self):
        print(f"Paying {self.amount} {self.currency}")

        
class CreditCardPayment:
    def __init__(self, amount, currency):
        super().__init__(amount, currency)
        self.amount = amount
        self.currency = currency

    def process(self):
        print(f"Paying {self.amount} {self.currency}")



# this is not bad, but we could use inheritance instead
class CreditCardPayment(Payment):
    def __init__(self, amount, currency, email):
        super().__init__(amount, currency)
        self.email = email

class PrimePayPalPayment(CreditCardPayment):
    def __init__(self, amount, currency, email, discount):
        super.__init__(amount, currency, email)
        self.discount = discount
        self.amount *= 1-self.discount/100

credit = CreditCardPayment(100, "usd", "test@email.it")
credit2 = CreditCardPayment(200, "eur", "test2@email.it")
issubclass(CreditCardPayment, Payment) # Check if one is a subclass of another class
isinstance(credit, CreditCardPayment)
credit = credit2
print(credit is credit2) # Check if two objects are the same thing

# polymorphism, the same method has different shapes based of when it gets called

class Payment:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def process(self):
        print(f"Paying {self.amount} {self.currency}")

    def engage_payment(self):
        print("Abilitating Payment...")
        self.process()

class Payment:
    def __init__(self, payment_service):
        self.payment_service = payment_service

    def process(self):
        self.payment_service.make_payment()

class CreditCardPayment:
    def make_payment(self):
        print("Paying via credit card")
  
class PaypalPayment:
    def make_payment(self):
        print("Paying via Paypal")

credit_card = CreditCardPayment()
paypal = PaypalPayment()

payment = Payment(paypal) # This property is called COMPOSITION