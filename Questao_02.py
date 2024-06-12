user_name = input('Nome de usuario: ')
password = input('Senha: ')
while user_name == password:
    user_name = input('Impossivel cadastrar nome e senha iguais...\nNome de usuario: ')
    password = input('Senha: ')
print('Conta cadastrada com sucesso.')