num = int(input('Digite um numero entre 1 e 10: '))
# Enqunto num for menor ou igual a 1 OU num menor ou igual a 10; O condigo sempre vai executar se uma das duas condicoes forem verdadeiras.
while num <= 1 or num <= 10:
    num = int(input('Valor invalido...\nDigite um numero entre 1 e 10: '))
for i in range(1, 10+1):
    print(f'{num} x {i} = {num*i}')