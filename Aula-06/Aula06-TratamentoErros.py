try:
    valor = int(input('Digite um valor inteiro: '))
    valor2 = int(input('Digite outro valor inteiro: '))
    valor3 = valor / valor2
    print(valor3)
except ValueError:    
    print('Não foi possivel converter o valor informado para um número inteiro')
except ZeroDivisionError:    
    print('Não foi possivel efetuar uma divisão por zero')    
except:
    print('Aconteceu um erro qualquer.') 