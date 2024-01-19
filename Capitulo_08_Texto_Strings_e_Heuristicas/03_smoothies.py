smoothies = ['coconut', 'strawberry', 'banana', 'pineapple', 'acai berry']

substring_01 = smoothies[2:4]
substring_02 = smoothies[:2]
substring_03 = smoothies[3:-1]

print(substring_01)
print(substring_02)
print(substring_03)

if 'coconut' in smoothies:
    print('Yes, they have coconut')
else:
    print('Oh well, no coconut today')
