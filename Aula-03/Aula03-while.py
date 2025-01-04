import os
import random

os.system('cls')
numero_secreto = random.randrange(0, 300000)
tentativas = 0

while tentativas < 5: #Executa enquanto a condição for verdadeira!
    tentativas += 1
    resp = int(input('Meu caro Tidas, diga um número de com quantos persas vamos lutar? '))

    if resp > numero_secreto:
        print('Errou! Um pouco menos!')
    elif resp < numero_secreto:
        print('Errou! Um pouco mais')
    elif resp == numero_secreto:
        print(f'Sim Tidas! Lutaremos contra {numero_secreto} persas! Ahul!')
        break

else:
    print(f'Tidas, lutaremos contra {numero_secreto} persas! Ahul!')
    print('Ohhh Leonidas... Tu tem que parar de arrumar essas tretas!')    