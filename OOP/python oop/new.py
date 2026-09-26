# duck typing

from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def __init__(self, payment_method_id):
        self.id = payment_method_id

    @abstractmethod
    def description(self):
        pass

class BkashPayment(PaymentMethod):
    def __init__(self, payment_method_id, phone_number):
        super().__init__(payment_method_id)
        self.phone_number = phone_number
    def description(self):
        return "Paid using bKash"

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



# doesnt inherit from payment method so still usabele

def show_payment_description(payment):
    print(payment.description())

show_payment_description(BkashPayment(110, "017xxxx"))
show_payment_description(CardPayment(210, "3456"))
show_payment_description(BankTransfer(310, "AB Bank"))

class CryptoPayment:
    def description(self):
        return "Paid using cryptocurrency"
        

show_payment_description(CryptoPayment())


#protocol

from typing import Protocol

