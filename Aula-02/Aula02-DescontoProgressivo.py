import os
os.system('cls')

valor_compra = input('Informe o valor da compra: ')

if not valor_compra=='':
    print(f'O tipo da variavel de valor_compra, ANTES da conversão é: {type(valor_compra)}')

    valor_compra = int(valor_compra)
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

    valorconsumido = valor_compra * desconto        
    print(f'O valor calculado foi de R${valorconsumido:.2f}. Onde a desconto foi de R${desconto:.2f} devido ao valor_compra de {valor_compra} WATTS ')    
else:
    print('O valor de valor_compra em WATTS é requerido')