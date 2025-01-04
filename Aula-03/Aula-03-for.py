import os
os.system('cls')

#Determinando o limite da lista
limite = 50

print(f'1. Gerando lista de 1 até {limite}')
for i in range(limite):
    if i+1 < limite:
        print(i+1, end=', ')
    else:
        print(i+1, end='.')

print('\n')
print(f'2. Gerando lista de {limite} a 1')
for i in range(limite, 0, -1):
    if i > 1:
        print(i, end=', ')
    else:
        print(i, end='.')   

print('\n')
print(f'3. Gerando lista de 1 até {limite}. Imprimindo apenas pares')
passo = 2 #A cada 2 passos, sempre teremos um valor par
for i in range(0, limite + passo, passo):
    if i < limite:
        print(i, end=', ')
    else:
        print(i, end='.')        

print('\n')
print(f'4. Gerando lista de preços da loja do Sr. Manoel Joaquim')
print(f'Lojas Quase Dois - Tabela de Preços')
for i in range(0, limite, 1):
    valor = (i + 1) * 1.99
    print(f'{i + 1:02} - R${valor:.2f}')
