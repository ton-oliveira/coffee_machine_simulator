coffee_machine = {'water': 400, 'milk': 540, 'coffee': 120, 'cups': 9, 'money': 550}
A = dict(buy='What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:',
         fill='fill',
         take='take')


def take():
    print(f'I gave you ${coffee_machine["money"]}')
    coffee_machine["money"] = 0

    menu()


def fill():
    print("Write how many ml of water do you want to add:")
    coffee_machine['water'] += int(input())
    print("Write how many ml of milk do you want to add:")
    coffee_machine['milk'] += int(input())
    print("Write how many grams of coffee beans do you want to add")
    coffee_machine['coffee'] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    coffee_machine['cups'] += int(input())

    menu()


def buy(choose):
    if choose == 1:
        espresso()
    elif choose == 2:
        latte()
    elif choose == 3:
        cappuccino()
    else:
        print("Wrong answer")


def espresso():
    coffee_machine['water'] -= 250
    coffee_machine['coffee'] -= 16
    coffee_machine['money'] += 4
    coffee_machine['cups'] -= 1

    menu()


def latte():
    coffee_machine['water'] -= 350
    coffee_machine['milk'] -= 75
    coffee_machine['coffee'] -= 20
    coffee_machine['money'] += 7
    coffee_machine['cups'] -= 1

    menu()


def cappuccino():
    coffee_machine['water'] -= 200
    coffee_machine['milk'] -= 100
    coffee_machine['coffee'] -= 12
    coffee_machine['money'] += 6
    coffee_machine['cups'] -= 1

    menu()


def menu():
    print(f'''
    The coffee machine has:
    {coffee_machine['water']} of water
    {coffee_machine['milk']} of milk
    {coffee_machine['coffee']} of coffee beans
    {coffee_machine['cups']} of disposable cups
    {coffee_machine['money']} of money
''')

menu()

action = input("write action (buy, fill, take):").lower()
print(A[action])

if action == "fill":
    fill()
elif action == "take":
    take()
elif action == "buy":
    user_action = int(input())
    buy(user_action)