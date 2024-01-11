#menu = ['Pizza', 'Pasta', 'Soup', 'Salad']

menu = []

menu.append('Burger')
menu.append('Sushi')
print(menu)

del menu[0]
print(menu)

menu.extend(['BBQ', 'Takos'])
print(menu)

menu = menu + ['BBQ', 'Takos']
print(menu)

menu.insert(1, 'Stir Fry')
print(menu)


mystery_01 = 'secret' * 5
print(mystery_01)

mystery_02 = ['secret'] * 5
print(mystery_02)
