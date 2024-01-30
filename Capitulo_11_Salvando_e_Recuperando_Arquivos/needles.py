for i in range(0, 1000):
    file_name = str(i) + '.txt'
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            if 'file_name' in text:
                print('Found file_name in file ' + str(i) + '.txt')
                print('Content of file ' + str(i) + '.txt:')
                print(text)
    except FileNotFoundError:
        pass  # Ignora o erro se o arquivo não for encontrado
    except PermissionError:
        print('Permission denied for file ' + str(i) + '.txt')
    except Exception as e:
        print('Error while processing file ' + str(i) + '.txt:', str(e))

print('Scan complete!')
