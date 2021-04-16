class Budget:
    def __init__(self):
        self.balance_food = 0
        self.balance_clothing = 0
        self.balance_entertainment = 0

    def total_amount(self):
        return self.balance_food + self.balance_clothing + self.balance_entertainment

    #methods for food category
    def deposit_food(self, amount):
        self.balance_food += amount
        return self.balance_food

    def withdraw_food(self, amount):
        if self.balance_food >= amount:
            self.balance_food -= amount
            return amount
        else:
            return f'you have insufficient funds'
    def balance_food_check(self):
        return self.balance_food

    #methods for clothing category
    def deposit_clothing(self, amount):
        self.balance_clothing += amount
        return self.balance_clothing

    def withdraw_clothing(self, amount):
        if self.balance_clothing >= amount:
            self.balance_clothing -= amount
            return amount
        else:
            return f'you have insufficient funds'
    def balance_clothing_check(self):
        return self.balance_clothing

    # methods for entertainment category
    def deposit_entertainment(self, amount):
        self.balance_entertainment += amount
        return self.balance_entertainment

    def withdraw_entertainment(self, amount):
        if self.balance_entertainment >= amount:
            self.balance_entertainment -= amount
            return amount
        else:
            return f'you have insufficient funds'

    def balance_entertainment_check(self):
        return self.balance_entertainment

    #transfer between category functions
    def transfer_from_food_to_clothing(self, amount):
        if self.balance_food >= amount:
            self.balance_food -= amount
            self.balance_clothing += amount
            return f'{self.balance_clothing}, {self.balance_food}'
        else:
            print('sorry, you have insufficient funds to transfer, fund your account first')


    def transfer_from_clothing_to_food(self, amount):
        self.balance_clothing -= amount
        self.balance_food += amount
        return f'{self.balance_clothing}, {self.balance_food}'

    def transfer_from_food_to_entertainment(self, amount):
        self.balance_food -= amount
        self.balance_entertainment += amount
        return f'{self.balance_entertainment}, {self.balance_food}'

    def transfer_from_entertainment_to_food(self, amount):
        self.balance_entertainment -= amount
        self.balance_food += amount
        return f'{self.balance_entertainment}, {self.balance_food}'

    def transfer_from_entertainment_to_clothing(self, amount):
        self.balance_entertainment -= amount
        self.balance_clothing += amount
        return f'{self.balance_entertainment}, {self.balance_clothing}'

    def transfer_from_clothing_to_entertainment(self, amount):
        self.balance_clothing -= amount
        self.balance_entertainment += amount
        return f'{self.balance_clothing}, {self.balance_entertainment}'



budget = Budget()
'''
print(budget.deposit_food(7000))
print(budget.withdraw_food(5000))
print(budget.withdraw_food(500))
print(budget.balance_food_check())
'''
