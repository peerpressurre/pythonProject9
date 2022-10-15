import sys
try:
    size = int(input('->'))

    for i in range(size):
        for j in range(size):
            if i == 0 or j == 0 or i == size-1 or j == size-1:
                sys.stdout.write('*')
            else:
                sys.stdout.write(' ')
        print(' ')
except Exception as ex:
    print(f'Error: {ex}')