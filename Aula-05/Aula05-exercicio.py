#Importa bibliotecas com funções
import os

#Funções criadas para esse programa
#Função de Calculo do IMC
def f_imc(peso, altura):
    return peso / ( altura ** 2)

#Função de Caluladora - Soma
def f_soma(resultado, valorentrado):
    return resultado + valorentrado

#Função de Caluladora - Subtração
def f_subtrai(resultado, valorentrado):
    return resultado - valorentrado

#Função de Caluladora - Multiplicação
def f_multiplica(resultado, valorentrado):
    return resultado * valorentrado

#Função de Caluladora - Divisão
def f_divide(resultado, valorentrado):
    return resultado / valorentrado

## Daqui pra baixo, é o programa principal que consome as funções declaradas acima.
os.system('cls')
print(f_imc(96, 1.73)) #Consome o Calculo do IMC

#Cria uma mini calculadora
resultado = 0
valorentrado = 0
linicio = True
while True:
    lentrada = input('Digite um número ou uma operação matemática básica (+, -, *, /) ou "Q" para sair: ')

    if lentrada.upper() == 'Q':
        break
    elif lentrada == '+':
        resultado = f_soma(resultado, valorentrado)
        valorentrado = 0
    elif lentrada == '-':
        resultado = f_subtrai(resultado, valorentrado)
        valorentrado = 0
    elif lentrada == '*':
        resultado = f_multiplica(resultado, valorentrado)
        valorentrado = 0
    elif lentrada == '/':
        resultado = f_divide(resultado, valorentrado)   
        valorentrado = 0
    else:
        valorentrado = float(lentrada) 

        if linicio == True:
            resultado = valorentrado
            valorentrado = 0
            linicio = False
        else:
            pass    

    print(f'Seu resultado até o momento: {resultado}')