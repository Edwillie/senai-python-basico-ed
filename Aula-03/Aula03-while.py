contador = 0

while True: #Executa enquanto a condição for verdadeira!
    print(f'Contador em {contador}')

    resp = input('Continuo contando (Sim / Não)? ')
    if resp.upper() == 'S' or resp.upper() == 'SIM':
        contador += 1
    else:
        break