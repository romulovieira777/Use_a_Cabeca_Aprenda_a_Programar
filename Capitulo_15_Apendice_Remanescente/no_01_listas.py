a = [x + x for x in range(10)]
print(a)

lyric = ['I', 'saw', 'heard', 'on', 'you', 'the', 'wireless', 'back', 'in', '52']
a = [s[0] for s in lyric]
b = [s[0] for s in lyric if s[0] > 'm']
print(a)
print(b)
