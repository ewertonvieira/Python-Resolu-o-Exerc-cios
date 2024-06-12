nota = float(input('Digite nota: '))
while (nota < 0) or (nota > 10):
    nota = float(input('Nota informada é invalida....\nPorfavor informe a nota correta no intervalo de 0 a 10: '))
print('Nota valida')