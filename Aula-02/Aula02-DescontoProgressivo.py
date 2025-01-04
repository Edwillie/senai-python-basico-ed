import os
os.system('cls')

valor_compra = input('Informe o valor da compra: ')

if not valor_compra=='':
    print(f'O tipo da variavel de valor_compra, ANTES da conversão é: {type(valor_compra)}')

    valor_compra = float(valor_compra)
    print(f'O tipo da variavel de valor_compra, DEPOIS da conversão é: {type(valor_compra)}')

    if valor_compra <= 100:
        desconto = 0
    elif valor_compra <= 300:
        desconto = 0.10
    elif valor_compra <= 400:
        desconto = 0.15
    elif valor_compra >= 400:
        desconto = 0.20
    else:
        mensagem = f'Valor fora da faixa de descontos'            

    valordesconto = valor_compra * desconto 
    valorfinal = valor_compra - valordesconto       
    print(f'O valor com desconto foi de R${valorfinal:.2f}. Onde a desconto foi de R${valordesconto:.2f} devido ao valor_compra de R${valor_compra:.2f}.')    
else:
    print('O valor de valor_compra é requerido')