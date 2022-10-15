try:
    size = int(input('->'))
    size += 1

    for i in range(size):
        for j in range(size):
            if i == 0:
                print('i0', end='')
            else:
                if j == {size}:
                    print('js', end='')
                else:
                    if j == 0:
                        print('\nj0')
                    else:
                        if i == {size}:
                            print('is', end='')
                        else:
                            print('')
    print()
except Exception as ex:
    print(f'Error: {ex}')