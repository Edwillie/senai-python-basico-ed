#Declaração de importações
import os

#Funções desta rotina
#Funções sem retorno, recebendo argumento simples
def escreve_mensagem(texto):
    print(texto)

#Função que recebe, vários argumentos e proporciona um retorno.
def calc_somar(num1, num2):
    soma = num1 + num2   

    return soma 

os.system('cls')
escreve_mensagem('Passei por aqui') #Funçao criada internamente

escreve_mensagem(calc_somar(10, 15)) #Usa as duas funções criadas internamente