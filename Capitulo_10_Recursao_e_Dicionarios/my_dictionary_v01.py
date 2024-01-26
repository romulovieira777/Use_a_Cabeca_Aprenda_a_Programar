my_dictionary = {}

my_dictionary['jenny'] = '867-5309'
my_dictionary['paul'] = '555-1201'
my_dictionary['david'] = '321-6617'
my_dictionary['jamie'] = '771-0091'
my_dictionary['paul'] = '443-0000'

phone_number = my_dictionary['jenny']
print("Jenny's phone number is", phone_number)

my_dictionary['age'] = 27
my_dictionary[42] = 'answer'
my_dictionary['scores'] = [92, 87, 99]

del my_dictionary['david']
print(my_dictionary)

if 'jenny' in my_dictionary:
    print('Found her!', my_dictionary['jenny'])
else:
    print('I need to get her number.')


for key in my_dictionary:
    print(key, ':', my_dictionary[key])

print(my_dictionary)
