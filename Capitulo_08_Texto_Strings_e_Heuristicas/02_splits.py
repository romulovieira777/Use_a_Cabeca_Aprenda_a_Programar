lyrics = 'I heard you on the wireless back in fifty two'
words = lyrics.split()
print(words)

for char in lyrics:
    print(char)

if 'wireless' in lyrics:
    print('Yes, they have wireless')
else:
    print('Oh well, no wireless today')
