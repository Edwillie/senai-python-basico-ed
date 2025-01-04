import os
import time
os.system('cls')

check_user = '######@#####.com'
check_senha = 'senha'

usuario = ''
senha = ''

tentativas = 1

while check_user != usuario and check_senha != senha and tentativas <=3:
    usuario = input('Informe seu usuário: ')
    senha = input('Informe sua senha: ')

    if check_user == usuario and check_senha == senha:
        print('Seja Bem-vindo!')
        break
    else:
        if (3 - tentativas) > 0:
            print(f'Incorreto!\nTente novamente! Você possui {3 - tentativas} tentativas restantes!')
            time.sleep(5)
            os.system('cls')
        else:
            print('Você falhou miseravelmente!')

        tentativas += 1

else:
    print('Sistema Bloqueado!')