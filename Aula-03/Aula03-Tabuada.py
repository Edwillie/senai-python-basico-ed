import os
os.system('cls')

#Entradas requeridas
tabuada = input('Qual tabuada deve ser gerada? ')
idx_inicio = input('Qual indice iniciar [1-10]? ')
idx_fim = input('Qual indice terminar [2-10]? ')

#Controle das entradas
if not tabuada == '' and not idx_inicio == '' and not idx_fim == '':
    tabuada = int(tabuada)
    idx_inicio = int(idx_inicio)
    idx_fim = int(idx_fim) 

    if (idx_inicio >= 1 and idx_inicio <= 10) and (idx_fim >= 1 and idx_fim <= 10):
        for i in range(idx_inicio, idx_fim + 1, 1):
            print(f'{tabuada} * {i} = {tabuada * (i) }')
    else:
        print('Você deve colocar os indices entre 1 e 10')
else:
    if tabuada == '':
        print(f'Você deveria ter informado: A tabuada desejada')    

    if idx_inicio == '':
        print(f'Você deveria ter informado: O indice de inicio')    

    if idx_fim == '':
        print(f'Você deveria ter informado: O indice de fim')    

