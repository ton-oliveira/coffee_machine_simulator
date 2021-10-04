def qtd_water(aqua):
    return aqua // 200


def qtd_milk(milk):
    return milk // 50


def qtd_beans(coffee):
    return coffee // 15


coffee_machine = []

water_ = int(input('Write how many ml of water the coffee machine has:'))
coffee_machine.append(qtd_water(water_))
milk_ = int(input('Write how many ml of milk the coffee machine has:'))
coffee_machine.append(qtd_milk(milk_))
coffee_b = int(input('Write how many grams of coffee beans the coffee machine has:'))
coffee_machine.append(qtd_beans(coffee_b))

cups_coffee = int(input('Write how many cups of coffee you will need:'))

check_coff = map(lambda x: x >= cups_coffee, coffee_machine)
one_more = min(coffee_machine) - cups_coffee

if all(list(check_coff)):
    if one_more > 0:
        print(f' Yes, I can make that amount of coffee ( and even {one_more} more than that)')
    print("Yes, I can make that amount of coffee")
else:
    print(f'No, I can make only {min(coffee_machine)}cups of coffee')