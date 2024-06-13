fnum = int(input('Primeiro numero do intervalo: '))
enum = int(input('Ultimo numero do intervalo: '))
print(", ".join(map(str, [num for num in range(fnum, enum+1)])))