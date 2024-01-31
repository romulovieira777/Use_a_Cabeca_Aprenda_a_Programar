for i in range(0, 1000):
    file_name = str(i) + '.txt'
    file = open(file_name, 'r')
    text = file.read()

    if 'needle' in text:
        print('Found needle in file ' + str(i) + '.txt')
    file.close()
