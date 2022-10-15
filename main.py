try:
   height = int(input('->'))
   length = int(input('->'))

   for i in range(height):
       for j in range(length):
           print('*', end='')
       print()
except Exception as ex:
    print(f'Error: {ex}')
