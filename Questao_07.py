maior = int(input("Numero: "))
for _ in range(4):
    nnum = int(input('Numero: '))
    if maior < nnum:
       maior = nnum
print(f'Maior numero dentre os cinco informados: {maior}')