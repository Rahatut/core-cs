class Expense:

    def __init__(
        self,
        id,
        user_id,
        amount,
        currency,
        category,
        description,    
    ):
        self.id=id
        self.user_id=user_id
        self.amount=amount
        self.currency=currency
        self.category=category
        self.description=description

    def summary(self):
        return f"{self.category}:{self.amount} {self.currency} - {self.description}"
    
    def change_category(self, new_category):
        self.category = new_category

    def after_discount(self, percentage):
        return self.amount * (1 - percentage / 100)

    def is_large(self):
        return self.amount>=1000

expense1 = Expense(1, 1, 350, "BDT", "Rent", "Monthly rent")
expense2 = Expense(2, 2, 450, "BDT", "Bills", "Monthly bills")
expense3 = Expense(3, 3, 350, "BDT", " Gas", "Monthly gas bill")

#method added

expense = Expense(
    1,
    1,
    1000,
    "BDT",
    "Electronics",
    "Keyboard"
)

new_amount = expense.after_discount(10)

#print(new_amount)

#print(expense1.__dict__)
#print(expense2.__dict__)
#print(expense3.__dict__)    

#print(expense1.summary())
        
# instance attribute vs class attribute

class Expense:

    DEFAULT_CURRENCY = "BDT" #class attribute

    def __init__(
        self,
        id,
        user_id,
        amount,
        currency,
        #category,
        description,    
    ):
        self.id=id
        self.user_id=user_id
        self.amount=amount
        self.currency=currency
        #self.category=category
        self.description=description
        
expense1 = Expense(1, 1, 350, "Rent", "Monthly rent")
expense2 = Expense(2, 2, 450, "Bills", "Monthly bills")


expense1.DEFAULT_CURRENCY = "USD" # accessible
print(expense1.DEFAULT_CURRENCY)
print(expense2.DEFAULT_CURRENCY)
print(Expense.DEFAULT_CURRENCY)

# encapsulation
#Python doesn't have Java-style private fields. Python generally relies on conventions and controlled interfaces.
# properties in python

class Expense:

    def __init__(self, amount):
        self._amount = amount ### note the underscore

    @property
    def amount(self):
        return self._amount ###

expense = Expense(500)

print(expense.amount)


#adding validation

class Expense:

    def __init__(self, amount):
        self.amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value<=0:
            raise ValueError("Expense amount must be positive")
        self._amount = value

expense = Expense(500)

print(expense.amount)    


#constructor, validation, class methods
class Expense:

    #SUPPORTED_CURRENCIES = {"BDT", "USD", "EUR"}

    def __init__(
        self,
        expense_id,
        user_id,
        amount,
        currency,
        category,
        description
    ):
        self.id = expense_id
        self.user_id = user_id
        self.amount = amount

        #if currency not in self.SUPPORTED_CURRENCIES:
            #raise ValueError("Unsupported currency")

        self.currency = currency
        self.category = category
        self.description = description

expense = Expense(
    1,
    42,
    500,
    "XYZ",
    "Food",
    "Lunch"
)

# if we receive data as dictionary from API/DB
data = {
    "id": 101,
    "user_id": 42,
    "amount": 500,
    "currency": "BDT",
    "category": "Food",
    "description": "Lunch"
}
# We could manually do:

expense = Expense(
    data["id"],
    data["user_id"],
    data["amount"],
    data["currency"],
    data["category"],
    data["description"]
)

# imagine this conversion is needed in many places.

class Expense:

    SUPPORTED_CURRENCIES = {"BDT", "USD", "EUR"}

    def __init__(
        self,
        expense_id,
        user_id,
        amount,
        currency,
        category,
        description
    ):
        self.id = expense_id
        self.user_id = user_id
        self.amount = amount
        self.currency = currency
        self.category = category
        self.description = description

    def summary(self):
        return f"{self.category}: {self.amount} {self.currency} - {self.description}"

    def is_large(self):
        return self.amount >= 1000

    def change_category(self, new_category):
        self.category = new_category

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["user_id"],
            data["amount"],
            data["currency"],
            data["category"],
            data["description"]
        )

data = {
    "id": 101,
    "user_id": 42,
    "amount": 500,
    "currency": "BDT",
    "category": "Food",
    "description": "Lunch"
}

expense = Expense.from_dict(data)

#Suppose we want to create an expense from a CSV row:

row = "101,42,500,BDT,Food,Lunch"
class Expense:

    SUPPORTED_CURRENCIES = {"BDT", "USD", "EUR"}

    def __init__(
        self,
        expense_id,
        user_id,
        amount,
        currency,
        category,
        description
    ):
        self.id = expense_id
        self.user_id = user_id
        self.amount = amount
        self.currency = currency
        self.category = category
        self.description = description

    def summary(self):
        return f"{self.category}: {self.amount} {self.currency} - {self.description}"

    def is_large(self):
        return self.amount >= 1000

    def change_category(self, new_category):
        self.category = new_category

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["user_id"],
            data["amount"],
            data["currency"],
            data["category"],
            data["description"]
        )
    @classmethod
    def from_csv(cls, row):
        parts = row.split(",") ## row splitted

        return cls(
            int(parts[0]), ##each row data
            int(parts[1]),
            float(parts[2]),
            parts[3],
            parts[4],
            parts[5]
        )

#Now the class has multiple alternative constructors: , right, classes can have multiple constructors

'''Expense(...)
    normal constructor

Expense.from_dict(...)
    construct from dictionary

Expense.from_csv(...)
    construct from CSV'''


# static methods
class Expense:

    SUPPORTED_CURRENCIES = {"BDT", "USD", "EUR"}

    def __init__(
        self,
        expense_id,
        user_id,
        amount,
        currency,
        category,
        description
    ):
        self.id = expense_id
        self.user_id = user_id
        self.amount = amount
        self.currency = currency
        self.category = category
        self.description = description

    def summary(self):
        return f"{self.category}: {self.amount} {self.currency} - {self.description}"

    def is_large(self):
        return self.amount >= 1000

    def change_category(self, new_category):
        self.category = new_category

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["user_id"],
            data["amount"],
            data["currency"],
            data["category"],
            data["description"]
        )
    @staticmethod
    def is_supported_currency(currency):
        return currency in Expense.SUPPORTED_CURRENCIES

    @classmethod
    def supported_curr(cls):
        return cls.SUPPORTED_CURRENCIES

Expense.is_supported_currency("BDT")

print(Expense.is_supported_currency("BDT"))
# True

print(Expense.is_supported_currency("XYZ"))
# False
print(Expense.supported_curr())
# False