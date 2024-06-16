fat = 1
ta = int(input('Informe numero para calculo de fatorial: '))
while True:
    if ta < 0 and ta > 16:
        print('Numero invalido...')
    while ta >= 1:
        fat = fat * ta
        ta -= 1
    print(fat)
    break