year = int(input('Внеси година во формат yyyy:'))


if (year%400  == 0 and year%100 == 0):
        print(f'{year} година е престапна година')
elif (year%4  == 0 and year%100 !=0):
        print(f'{year} година е престапна година')
else:
    print(f'{year} година не е престапна година')


