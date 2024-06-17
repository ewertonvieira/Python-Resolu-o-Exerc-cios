primos = []
numb = int(input('Digite um numero: '))

for num in range(2, numb):  # Começa de 2, pois 1 não é primo
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break  # Se encontrou um divisor, não é primo
        else:
            primos.append(num)  # Se o loop terminou sem break, o número é primo

print(f'Os números primos até {numb} são: {primos}')
