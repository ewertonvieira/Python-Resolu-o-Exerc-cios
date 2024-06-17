verificador = True
numdiv = []
num = int(input('Informe um numero: '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            verificador = False
            numdiv.append(i)
    verificador = False
print('PRIMO'if verificador == True else f'Não é primo pois é divisivel por: {', '.join(map(str,numdiv))}')