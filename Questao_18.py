maior = 0
menor = 0
soma = 0
while True:
    num = int(input('Valor: '))
    cont = input('Deseja continuar[s/n]??? ').upper()
    # Define o maior numero comparando a zero
    if maior == 0 or num > maior:
        maior = num
    else:
        menor = num
    if num < menor:
        menor = num
    soma += num
    if cont == 'N':
        break
print(f'Maior {maior}\nMenor {menor}\nSoma {soma}')