coffee_machine = {'water': 400, 'milk': 540, 'coffee': 120, 'cups': 9, 'money': 550}
A = dict(buy='What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ',
         fill='fill', take='take', remaining='remaining', exit='exit')
B = {0: 'Sorry, not enough water', 1: 'Sorry, not enough coffee beans', 2: 'Sorry, not enough cups', 3: 'Sorry, not enough milk'}


def take():
    print(f'I gave you ${coffee_machine["money"]}')
    coffee_machine["money"] = 0


def fill():
    print("Write how many ml of water do you want to add:")
    coffee_machine['water'] += int(input())
    print("Write how many ml of milk do you want to add:")
    coffee_machine['milk'] += int(input())
    print("Write how many grams of coffee beans do you want to add")
    coffee_machine['coffee'] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    coffee_machine['cups'] += int(input())


def check_espresso():
    check = coffee_machine.copy()
    test = [check['water'] >= 250, check['coffee'] >= 16, check['cups'] >= 1]
    if all(test):
        espresso()
    else:
        miss = test.index(False)
        print(B.get(miss))


def check_late():
    check = coffee_machine.copy()
    test = [check['water'] >= 350, check['coffee'] >= 20, check['cups'] >= 1, check['milk'] >= 75]
    if all(test):
        latte()
    else:
        miss = test.index(False)
        print(B.get(miss))


def check_cappuccino():
    check = coffee_machine.copy()
    test = [check['water'] >= 200, check['coffee'] >= 12, check['cups'] >= 1, check['milk'] >= 100]
    if all(test):
        cappuccino()
    else:
        miss = test.index(False)
        print(B.get(miss))


def buy(choose):
    if choose == '1':
        check_espresso()
    elif choose == '2':
        check_late()
    elif choose == '3':
        check_cappuccino()
    else:
        pass


def espresso():
    coffee_machine['water'] -= 250
    coffee_machine['coffee'] -= 16
    coffee_machine['money'] += 4
    coffee_machine['cups'] -= 1


def latte():
    coffee_machine['water'] -= 350
    coffee_machine['milk'] -= 75
    coffee_machine['coffee'] -= 20
    coffee_machine['money'] += 7
    coffee_machine['cups'] -= 1


def cappuccino():
    coffee_machine['water'] -= 200
    coffee_machine['milk'] -= 100
    coffee_machine['coffee'] -= 12
    coffee_machine['money'] += 6
    coffee_machine['cups'] -= 1


def menu():
    print(f'''
    The coffee machine has:
    {coffee_machine['water']} of water
    {coffee_machine['milk']} of milk
    {coffee_machine['coffee']} of coffee beans
    {coffee_machine['cups']} of disposable cups
    {coffee_machine['money']} of money
''')


while True:
    action = input("Write action (buy, fill, take, remaining, exit):").lower()
    print(A[action])
    if action == "fill":
        fill()
    elif action == "take":
        take()
    elif action == "buy":
        user_action = input()
        buy(user_action)
    elif action == 'exit':
        break
    elif action == 'remaining':
        menu()
        