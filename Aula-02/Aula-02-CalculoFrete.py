import os
os.system('cls')

valor_compra = input('Informe o valor da compra: ')
km_distancia = input('Informe a distancia de entrega (KM): ')

if not valor_compra=='' and not km_distancia=='':
    #Ajustando tipagem dos valores para prosseguir
    valor_compra = float(valor_compra)
    km_distancia = float(km_distancia)

    #Calcula o valor do frete
    if km_distancia <= 50:
        valor_frete = 1
    else:
        valor_frete = 1.5

    frete_calculado = km_distancia * valor_frete

    #Verifica se compra é elegível para frete gratis
    if valor_compra >= 200:
        frete_compra = 0
        msg_frete = 'frete grátis'
    else:
        frete_compra = frete_calculado
        msg_frete = f'valor do frete calculado em {frete_compra:.2f}. Onde a distancia informada, possui uma tarifa de {valor_frete:.2f}/km'

    valor_final = valor_compra + frete_compra       

    print(f'Sua compra teve o valor de R${valor_final:.2f}. Você teve {msg_frete}')
else:
    print('Ambos valores requisitados devem ser preenchidos.')