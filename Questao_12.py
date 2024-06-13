inicio = int(input('Digite primeiro numero: '))
fim = int(input('Digite segundo numero: '))

if inicio == fim:
    print('Intervalo inteiro inexistente...')
elif inicio < fim:
    inicio += 1
    if inicio - fim == 0:
        print('Intervalo inteiro inexistente...')
    else:
        print([i for i in range(inicio, fim)])
elif inicio > fim:
    inicio -= 1
    if fim - inicio == 0:
        print('Intervalo inteiro inexistente...')
    else:
        print([k for k in range(inicio, fim, -1)])