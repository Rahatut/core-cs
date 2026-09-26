class User:
    def __init__(self, user_id, name, email):
        self.id = user_id
        self.name = name
        self.email = email
    def display_name(self):
        return f"{self.name} <{self.email}>"

user = User(
    1,
    "Rahatut",
    "rahatut@example.com"
)

class PaymentMethod:
    def __init__(
        self,
        payment_method_id,
        method_type    
    ):
        self.payment_method_id=payment_method_id
        self.method_type=method_type

    def description(self):
        return f"Paid using {self.method_type}"

payment_method = PaymentMethod(
    101,
    "bKash"
)

class Expense:
    def __init__(
        self,
        expense_id,
        user,
        amount,
        currency,
        category,
        description,
        payment_method
    ):
        self.id = expense_id
        self.user = user
        self.amount = amount
        self.currency = currency
        self.category = category
        self.description = description
        self.payment_method=payment_method
    def summary(self):
        return f"{self.user.display_name()} {self.payment_method.description()} | {self.currency}{self.amount} for {self.description}"


#An object can contain other objects.
expense = Expense(101, user, 350, "BDT", "food", "Lunch", payment_method)

print(expense.user.name)
print(expense.payment_method.method_type)
print(expense.summary())