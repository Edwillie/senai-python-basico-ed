import os
os.system('cls')  #Limpa a tela antes de iniciar os comando do programa

print('###### CALCULO DO IMC ######')
peso = float(input('Entre com seu peso em Kilos: '))
altura_m = float(input('Entre com sua altura em metros: '))

imc = peso / (altura_m ** 2)

print(f'Seu IMC é {round(imc,2)}!')

if imc <= 18.5:
    print('Chassi de grilo! Abaixo do peso ideal')
elif imc <= 24.9:    
    print('Magrelo! Peso ideal')
elif imc <= 29.9:    
    print('Opa, presta atenção! Levemente acima do peso')    
elif imc <= 34.9:    
    print('Tá na hora de buscar uma academia! Obesidade Grau 1')        
elif imc <= 39.9:    
    print('Joga fora esse chocolate! Obesidade Grau 2 (severa)')            
else:
    print('Ferrou! Obesidade Grau 3 (morbida)')                
