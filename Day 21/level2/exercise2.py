# Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties
# and it has total_income, total_expense, account_info, add_income, add_expense and
# account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.

class PersonAccount:

    def __init__(self, firstName, lastName, income = 0, expense = 0):
        self.firstName = firstName
        self.lastName = lastName
        self.income = income
        self.expense = expense

    def account_info(self):
        return f"This account belongs to {self.firstName}  {self.lastName}"


    def total_worth(self):
        total_networth = self.income - self.expense

account = PersonAccount("Dennis", "Njogu", 2300, 900)
print(account.total_worth())