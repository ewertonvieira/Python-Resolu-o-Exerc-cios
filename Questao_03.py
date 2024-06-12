nome = input('Nome: ')
idade = int(input('Idade: '))
salario = float(input('Salário: '))
sexo = input('Sexo [F - feminino | M - masculino]: ').lower()
estado_civil = input('Estado civil [S - solteiro(a) | C - casado(a) | V - viúvo(a) | D - divorciado(a)]: ').lower()

# Inicializando as variáveis de verificação como False
n = i = sa = se = esc = False

while True:
    if len(nome) < 4:
        nome = input('Nome inválido, tente novamente.\nNome: ')
    else:
        n = True

    if idade < 0 or idade > 150:
        idade = int(input('Idade inválida, tente novamente.\nIdade: '))
    else:
        i = True

    if salario <= 0:
        salario = float(input('Salário inválido, tente novamente.\nSalário: '))
    else:
        sa = True

    if sexo not in ['f', 'm']:
        sexo = input('Sexo informado inválido, tente novamente.\nSexo [F - feminino | M - masculino]: ').lower()
    else:
        se = True

    if estado_civil not in ['s', 'c', 'v', 'd']:
        estado_civil = input('Estado civil com valor inválido, tente novamente.\nEstado civil [S - solteiro(a) | C - casado(a) | V - viúvo(a) | D - divorciado(a)]: ').lower()
    else:
        esc = True

    if all([n, i, sa, se, esc]):
        break

print('Cadastro validado!')

#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd';