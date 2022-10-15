try:
   size = int(input('->'))

   for i in range(size):
       for j in range(size):
           print('*', end='')
       print()
except Exception as ex:
    print(f'Error: {ex}')