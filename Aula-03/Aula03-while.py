condicao = True
contador = 0

while condicao:
    print(f'Contador em {contador}')

    resp = input('Continuo contando (Sim / Não)? ')
    if resp.upper() == 'S' or resp.upper() == 'SIM':
        contador = contador + 1
    else:
        condicao = False   