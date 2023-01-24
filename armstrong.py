'''
    This code calcule the Number of Armstrong, than say: 
    the "len()" of a number is the sum of your numbers
    Ex: 153 = 1³ + 5³ + 3³ ;
    1 + 125 + 27 = 153
'''

limit = input('Set the limit of a "Numbers of Armstrong" to print.\n>  ')

try:
    int(limit)
except TypeError:
    print("This number is'nt integer.")

for i in range(1, int(limit)):
    sumer = 0
    conta = ...
    letter = str(i)
    inLen = len(letter)

    for j in str(i):
        conta = int(j)**inLen
        sumer += conta
        six = len(letter) <= 6
        if int(sumer) == i and six:
            print(i)
            break 
        else:
            continue