import os
os.system('cls')

consumo = input('Informe o consumo em WATTS: ')

if not consumo=='':
    print(f'O tipo da variavel de consumo, ANTES da conversão é: {type(consumo)}')

    consumo = int(consumo)
    print(f'O tipo da variavel de consumo, DEPOIS da conversão é: {type(consumo)}')

    if consumo <= 100:
        tarifa = 0.65
    elif consumo <= 150:
        tarifa = 0.70
    elif consumo <= 200:
        tarifa = 0.75
    else:
        tarifa = 0.80        

    valorconsumido = consumo * tarifa        
    print(f'O valor calculado foi de R${valorconsumido:.2f}. Onde a tarifa foi de R${tarifa:.2f} devido ao consumo de {consumo} WATTS ')    
else:
    print('O valor de consumo em WATTS é requerido')