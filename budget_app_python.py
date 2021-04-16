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
count = 5
while True:
    print('what do you want to do? ')
    for i in range(5):
        try:
            category_input = int(input('\nFor Deposit: press 1: \nFor withdrawal: press 2: \nFor Balance: press 3: \nFor Transfer: press 4: \nEnter choice: '))
            #print(category_input)
        except ValueError:
            count = count - 1
            print(f'please enter a number to continue, you have {count} more attempts remaining to quit the program ')
        else:
            if category_input == 0:
                break
            elif category_input == 1:
                category_deposit = int(input('choose a category you want to fund (deposit)? \nFood category: press 1: \nClothing category: press 2: \nEntertainment category: press 3: \nEnter your choice: '))
                #condition to check if deposit is for food
                if category_deposit == 1:
                    food_category_deposit = int(input('enter the amount you want to deposit into your food wallet: '))
                    amount_deposited_to_food = budget.deposit_food(food_category_deposit)
                    print(f'you have funded your food wallet with {food_category_deposit}, balance is {budget.balance_food_check()}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
                # condition to check if deposit is for clothing
                elif category_deposit == 2:
                    clothing_category_deposit = int(input('enter the amount you want to deposit into your clothing wallet: '))
                    amount_deposited_to_clothing = budget.deposit_clothing(clothing_category_deposit)
                    print(f'you have funded your clothing wallet with {clothing_category_deposit}, balance is {budget.balance_clothing_check()}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
                elif category_deposit == 3:
                    entertainment_category_deposit = int(input('enter the amount you want to deposit into your entertainment wallet: '))
                    amount_deposited_to_entertainment = budget.deposit_entertainment(entertainment_category_deposit)
                    print(f'you have funded your entertainment wallet with {entertainment_category_deposit}, balance is {budget.balance_entertainment_check()}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
            elif category_input == 2:
                category_withdraw = int(input('choose a category you want to withraw from? \nFood category: press 1: \nClothing category: press 2: \nEntertainment category: press 3: \nEnter your choice: '))
                # condition to check if withdrawal is for food
                if category_withdraw == 1:
                    food_category_withdraw = int(input('enter the amount you want to withdraw from your food wallet: '))
                    amount_withdrawn_from_food = budget.withdraw_food(food_category_withdraw)
                    print(f'You have withdrawn {amount_withdrawn_from_food} from your food wallet, balance is {budget.balance_food_check()}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
                # condition to check if withdrawal is for clothing
                elif category_withdraw == 2:
                    clothing_category_withdraw = int(input('enter the amount you want to withdraw from your clothing wallet: '))
                    amount_withdrawn_from_clothing = budget.withdraw_clothing(clothing_category_withdraw)
                    print(f'You have withdrawn {amount_withdrawn_from_clothing} from your clothing wallet, balance is {budget.balance_clothing_check()}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
                elif category_withdraw == 3:
                    entertainment_category_withdraw = int(input('enter the amount you want to withdraw from your entertainment wallet: '))
                    amount_withdrawn_from_entertainment = budget.withdraw_entertainment(entertainment_category_withdraw)
                    print(f'You have withdrawn {amount_withdrawn_from_entertainment} from your entertainment wallet, balance is {budget.balance_entertainment_check()}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
            elif category_input == 3:
                category_balance = int(input('choose a category you want to check balance from? \nFood category: press 1: \nClothing category: press 2: \nEntertainment category: press 3: \nEnter your choice: '))
                # condition to check balance for food
                if category_balance == 1:
                    food_category_balance = budget.balance_food_check()
                    print(f'The current balance in your food wallet is, {food_category_balance}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
                elif category_balance == 2:
                    clothing_category_balance = budget.balance_clothing_check()
                    print(f'The current balance in your clothing wallet is, {clothing_category_balance}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
                elif category_balance == 3:
                    entertainment_category_balance = budget.balance_entertainment_check()
                    print(f'The current balance in your entertainment wallet is, {entertainment_category_balance}')
                    exit_option = input('type yes or click the enter button to continue or type stop to end transaction: ')
                    if exit_option == '' or 'yes':
                        continue
                    elif exit_option == 'stop':
                        print('have  nice day')
                        break
            elif category_input == 4:
                category_transfer_from = int(input('choose a category you want to transfer from? \nFood category: press 1: \nClothing category: press 2: \nEntertainment category: press 3: \nEnter your choice: '))
                if category_transfer_from == 1:
                    category_transfer_to = int(input('choose a category you want to transfer to? \nClothing category: press 2: \nEntertainment category: press 3: \nEnter your choice: '))
                    if category_transfer_to == 2:
                        print('you are about to from your food budget to your clothing budget')
                        transfer_amount = int(input('enter amount you want to transfer: '))
                        category_transfer_from_food = budget.transfer_from_food_to_clothing(transfer_amount)
                        print(f'you now have {budget.balance_clothing_check()} for clothing budget')
                        print(f'{budget.balance_food_check()} is left in the food budget')
                    elif category_transfer_to == 3:
                        print('you are about to from your food budget to your entertainment budget')
                        transfer_amount = int(input('enter amount you want to transfer: '))
                        category_transfer_from_food = budget.transfer_from_food_to_entertainment(transfer_amount)
                        print(f'you now have {budget.balance_entertainment_check()} for clothing budget')
                        print(f'{budget.balance_food_check()} is left in the food budget')
                elif category_transfer_from == 2:
                    category_transfer_to = int(input('choose a category you want to transfer to? \nfood category: press 2: \nEntertainment category: press 3: \nEnter your choice: '))
                    if category_transfer_to == 2:
                        print('you are about to transfer from your clothing budget to your food budget')
                        transfer_amount = int(input('enter amount you want to transfer: '))
                        category_transfer_from_clothing = budget.transfer_from_clothing_to_food(transfer_amount)
                        print(f'you now have {budget.balance_clothing_check()} for clothing budget')
                        print(f'{budget.balance_food_check()} is left in the food budget')
                    elif category_transfer_to == 3:
                        print('you are about to transfer from your clothing budget to your entertainment budget')
                        transfer_amount = int(input('enter amount you want to transfer: '))
                        category_transfer_from_clothing = budget.transfer_from_clothing_to_entertainment(transfer_amount)
                        print(f'you now have {budget.balance_clothing_check()} for clothing budget')
                        print(f'{budget.balance_entertainment_check()} is left in the entertainment budget')
                elif category_transfer_from == 3:
                    category_transfer_to = int(input('choose a category you want to transfer to? \nfood category: press 2: \nclothing category: press 3: \nEnter your choice: '))
                    if category_transfer_to == 2:
                        print('you are about to transfer from your entertainment budget to your food budget')
                        transfer_amount = int(input('enter amount you want to transfer: '))
                        category_transfer_from_entertainment = budget.transfer_from_entertainment_to_food(transfer_amount)
                        print(f'you now have {budget.balance_entertainment_check()} for clothing budget')
                        print(f'{budget.balance_food_check()} is left in the food budget')
                    elif category_transfer_to == 3:
                        print('you are about to transfer from your entertainment budget to your clothing budget')
                        transfer_amount = int(input('enter amount you want to transfer: '))
                        category_transfer_from_entertainment = budget.transfer_from_entertainment_to_clothing(transfer_amount)
                        print(f'you now have {budget.balance_entertainment_check()} for entertainment budget')
                        print(f'{budget.balance_clothing_check()} is left in the clothing budget')




