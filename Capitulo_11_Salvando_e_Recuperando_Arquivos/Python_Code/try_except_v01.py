try:
    filename = 'nottthere.txt'
    file = open(filename, 'r')
except:
    print('Soory, an error ocurred opening', filename)
else:
    print('Glad we got that file open')
    file.close()
