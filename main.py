try:
    length = int(input('->'))
    width = int(input('->'))

    for i in range(length):
        for j in range(width):
            if i == 0 or j == 0 or i == length-1 or j == width-1:
                print('* ', end=' ')
            else:
                print('  ', end=' ')
        print(' ')
except Exception as ex:
    print(f'Error: {ex}')