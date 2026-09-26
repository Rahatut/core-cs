#Whats an object?
# a dictionary can be used to represent - suppose Expenses
expense = {
    "id": 101,
    "user_id": 42,
    "amount": 350,
    "currency": "BDT",
    "category": "food",
    "description": "Lunch"
}
# but, for thousands of such examples, where expense need to be used - interconnection between operations exist, oop connects data and behaviour

class Expense:
    pass

expense = Expense()

class Expense:
    pass


expense = Expense()

expense.id = 101
expense.user_id = 42
expense.amount = 350
expense.currency = "BDT"
expense.category = "food"
expense.description = "Lunch"


print(expense.__dict__) # inspect all data


#everytime we create expense object, manually need to assign. pera

#solution - __init__ 

def __init__(
    self,
    id,
    user_id,
    amount,
    currency,
    category,
    description
): 
    self.id = id
    self.user_id = user_id
    self.amount = amount
    self.currency = currency
    self.category = category
    self.description = description


expense1 = Expense(101, 42, 350, "BDT", "food", "Lunch")
expense2 = Expense(102, 42, 1200, "BDT", "transport", "Uber")