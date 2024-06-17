count = 0
primos = []
numb = int(input('Digite um numero: '))

for num in range(3, numb):
    notprimo = False
    for i in range(2, num):
        if num % i == 0:
            count += 1
            notprimo = True
            break
    if notprimo == False:
        primos.append(num)

print(f'Os números primos até {numb} são: {primos}, numero de divisoes: {count}')
