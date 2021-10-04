class CoffeeMachine:
    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550
    B = {0: 'Sorry, not enough water', 1: 'Sorry, not enough coffee beans', 2: 'Sorry, not enough cups'}

    def take(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def fill(self):
        print("Write how many ml of water do you want to add:")
        self.water += int(input())
        print("Write how many ml of milk do you want to add:")
        self.milk += int(input())
        print("Write how many grams of coffee beans do you want to add")
        self.coffee += int(input())
        print("Write how many disposable cups of coffee do you want to add:")
        self.cups += int(input())

    def check_espresso(self):
        check_machine = {'water': self.water, 'coffee': self.coffee, 'cups': self.cups}
        test = [check_machine['water'] >= 250, check_machine['coffee'] >= 16, check_machine['cups'] >= 1]
        if all(test):
            self.espresso()
        else:
            miss = test.index(False)
            print(self.B.get(miss) + '\n')

    def espresso(self):
        self.water -= 250
        self.coffee -= 16
        self.money += 4
        self.cups -= 1

    def check_late(self):
        check_machine = {'water': self.water, 'coffee': self.coffee, 'cups': self.cups, 'milk': self.milk}
        test = [check_machine['water'] >= 350, check_machine['coffee'] >= 20, check_machine['cups'] >= 1, check_machine['milk'] >= 75]
        if all(test):
            self.late()
        else:
            miss = test.index(False)
            print(self.B.get(miss) + '\n')

    def late(self):
        self.water -= 350
        self.milk -= 75
        self.coffee -= 20
        self.money += 7
        self.cups -= 1

    def check_cappuccino(self):
        check_machine = {'water': self.water, 'coffee': self.coffee, 'cups': self.cups, 'milk': self.milk}
        test = [check_machine['water'] >= 200, check_machine['coffee'] >= 12, check_machine['cups'] >= 1, check_machine['milk'] >= 100]
        if all(test):
            self.cappuccino()
        else:
            miss = test.index(False)
            print(self.B.get(miss) + '\n')

    def cappuccino(self):
        self.water -= 200
        self.milk -= 100
        self.coffee -= 12
        self.money += 6
        self.cups -= 1

    def menu(self):
        return '''\nThe coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money \n'''.format(self.water, self.milk, self.coffee, self.cups, self.money)

    def buy(self, choose):
        if choose == '1':
            self.check_espresso()
        elif choose == '2':
            self.check_late()
        elif choose == '3':
            self.check_cappuccino()
        else:
            pass


q = CoffeeMachine()

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input().lower()
    if action == "fill":
        q.fill()
    elif action == "take":
        q.take()
    elif action == "buy":
        print('\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        user_action = input()
        q.buy(user_action)
    elif action == 'exit':
        break
    elif action == 'remaining':
        print(q.menu())
