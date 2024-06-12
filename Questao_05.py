count = 0
cidade_a = float(input('Informe polucacao da primeira cidade: '))
tax_a = float(input('Informe taxa de crescimento da primeira cidade: '))
cidade_b = float(input('Informe polucacao da segunda cidade: '))
tax_b = float(input('Informe taxa de crescimento da segunda cidade: '))
print('*'*57)
if cidade_a > cidade_b:
    while cidade_b < cidade_a:
        cidade_b += cidade_b * tax_b
        cidade_a += cidade_a * tax_a
        count += 1
    print(f'{count} anos para Cidade-B superar a Cidade-A em populacao... ')
else:
    while cidade_a < cidade_b:
        cidade_a += cidade_a * tax_a
        cidade_b += cidade_b * tax_b
        count += 1
    print(f'{count} anos para Cidade-A superar a Cidade-B em populacao... ')