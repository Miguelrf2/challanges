from random import randint
import bisect

numbers  = []

for i in range(100):
    numbers.append(randint(0, 1000))

while True:
    num = input('Choose a number to search in list. \n')
    numbers.sort()
    if num == 'verify': #It is for tests.
        print(numbers)

    if int(num) in numbers:
        indice = bisect.bisect_left(numbers, int(num))
        print(f'Número encontrado na posição {indice}')
    else:
        print(-1)
        for i in numbers:
            print(i)