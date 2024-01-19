lyrics = 'I heard you on the wireless back in fifty two'
words = lyrics.split()
my_substring_01 = lyrics[2:7]
my_substring_02 = lyrics[:6]
my_substring_03 = lyrics[28:]
my_substring_04 = lyrics[28:-1]
my_substring_05 = lyrics[-17:]

print(words)
print(my_substring_01)
print(my_substring_02)
print(my_substring_03)
print(my_substring_04)
print(my_substring_05)


for char in lyrics:
    print(char)

if 'wireless' in lyrics:
    print('Yes, they have wireless')
else:
    print('Oh well, no wireless today')
