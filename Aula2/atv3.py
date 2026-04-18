# 3. Acesso ao sistema
# Enunciado:
# Leia o nome de usuário e a senha. O acesso é permitido apenas se o usuário 
# for "admin" e a senha for "1234".
# Use and para verificar as duas condições e exiba "Acesso liberado" 
# ou "Acesso negado".

usu = input('Digite seu usuário: ')
senha = int(input('Digite sua senha: '))

verificar = usu == 'admin' and senha == 1234 and 'Acesso liberado' or 'Acesso negado'

print(verificar)