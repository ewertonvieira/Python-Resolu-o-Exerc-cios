init = int(input('Digite um numero: '))
ending = int(input('Digite um numero: '))
# Faça um programa que receba dois números inteiros
# e gere os números inteiros que estão no intervalo compreendido por eles.
if init > ending:
    for i in range(init - 1, ending, -1):
        print(i)
elif ending + 1 > init:
    for i in range(init + 1, ending):
        print(i)
else:
    print('Não há intervalo entre os números fornecidos.')
