smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']

length = len(smoothies)
last = smoothies[length - 1]
print(last)

last_1 = smoothies[-1]
second_last = smoothies[-2]
third_last = smoothies[-3]
print(last_1)
print(second_last)
print(third_last)

smoothies[3] = 'pineapple'
print(smoothies)

smoothies = 'watermelon'
#recent = smoothies[most_recent]
print(smoothies)


smoothies = ['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']
has_coconut = [True, False, True, False, False]

for i in range(len(has_coconut)):
    if has_coconut[i]:
        print(smoothies[i], 'contains coconut')
