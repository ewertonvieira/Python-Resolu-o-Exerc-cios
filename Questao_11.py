soma = 0
fnum = int(input('Primeiro numero do intervalo: '))
enum = int(input('Ultimo numero do intervalo: '))
for aux in range(fnum, enum+1):
    soma += aux
print(soma)
