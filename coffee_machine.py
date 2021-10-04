print('''
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
''')

# calculate the amount of ingredients it needs
cups_coffee = int(input('Write how many cups of coffee you will need:'))
print(f'For {cups_coffee} cups of coffee you will need:')
print(f'{cups_coffee * 200} ml of water')
print(f'{cups_coffee * 50} ml of milk')
print(f'{cups_coffee * 15} g of coffee beans')