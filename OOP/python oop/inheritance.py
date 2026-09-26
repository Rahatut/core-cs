from abc import ABC, abstractmethod

# inheritance vs composition -
# obj inside obj - composition
# credcard payment is a payment method
# abstraction
# polymorphism

class PaymentMethod:
    def __init__(self, payment_method_id):
        self.id = payment_method_id

    def description(self):
        return "Generic payment method"

class BkashPayment(PaymentMethod):
    def __init__(self, payment_method_id, phone_number):
        super().__init__(payment_method_id)
        self.phone_number = phone_number
    def description(self):
        return "Paid using bKash"

payment = BkashPayment(101, "017XXXXXXXX")

print(payment.id)
print(payment.phone_number)
print(payment.description())

class CardPayment(PaymentMethod):
    def __init__(self, payment_method_id, last_four_digits):
        super().__init__(payment_method_id)
        self.last_four_digits = last_four_digits
    def description(self):
        return "Paid using Card"

class BankTransfer(PaymentMethod):
    def __init__(self, payment_method_id, bank_name):
        super().__init__(payment_method_id)
        self.bank_name = bank_name
    def description(self):
        return "Bank transfer"


payments = [
    BkashPayment(110, "017xxxx" ),
    CardPayment(210, "3456"),
    BankTransfer(310, "AB Bank")
]

for payment in payments:
    print(payment.description())

# abstract class - using pythons abc module
class PaymentMethod(ABC):
    def __init__(self, payment_method_id):
        self.id = payment_method_id

    @abstractmethod
    def description(self):
        pass

#Every concrete subclass of PaymentMethod must implement description().
class BkashPayment(PaymentMethod):
    def __init__(self, payment_method_id, phone_number):
        super().__init__(payment_method_id)
        self.phone_number = phone_number

    def description(self):
        return "Paid using bKash"
    
#payment = PaymentMethod(101)
#TypeError: Can't instantiate abstract class PaymentMethod without an implementation for abstract method 'description'

payments = [
    BkashPayment(110, "017xxxx" ),
    CardPayment(210, "3456"),
    BankTransfer(310, "AB Bank")
]
for payment in payments:
    print(payment.description())