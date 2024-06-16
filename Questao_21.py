verificador = True
num = int(input('Informe um numero: '))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            verificador = False
            break
else:
    verificador = False
print('PRIMO'if verificador == True else 'NAO PRIMO')