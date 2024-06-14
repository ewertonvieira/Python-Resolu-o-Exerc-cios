i = 0; countpar = 0; countimpar = 0
while i != 10:
    num = int(input('Digite numero: '))
    if num % 2 == 0:
        countpar += 1
    else:
        countimpar +=1
    i += 1
print(f'Quantidade de numeros pares: {countpar}\nQuantidade de numeros impares: {countimpar}')