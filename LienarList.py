numeros = [1, 2, 3, 4, 5, 6]

while True:
    search = input('Search for: ')

    toInt = int(search)
    if int(search) in numeros:
        print('search - ', numeros.index(toInt))
    else:
        print('-1')