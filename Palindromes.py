while True:
    text = input('Write a word or phrase.\n > ').lower()

    invert = text[::-1]

    if text == '.exit':
        break

    if invert == text:
        print(True)

    else:
        print(False)