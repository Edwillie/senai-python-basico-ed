#Bibliotecas
import os
import time

#Variaveis
listaNomes = []
indiceNomes = 0

#Coleta os nomes de Pessoas
while True:
    os.system('cls')
    nome = input('Insira um nome de uma pessoa: (ou pressione "Q", caso queira parar de inserir nomes) ')

    if nome.upper() == "Q":
        break
    elif nome.upper() == "NÃO" or nome.upper() == "SAIR":
        print('ATENÇÃO: Você usou palaras reservadas!')
        time.sleep(5)
    else:
        listaNomes.append(nome)

#Lista o nome das pessoas coletadas
os.system('cls')
print('Aqui está sua lista:')
for nome in listaNomes: 
    indiceNomes += 1
    print(f'{indiceNomes:02} : {nome}')

#Atua com o usuario para corrigir a lista
print('\n')
while True:
    NomeOrig = input('Há algum nome para corrigir na lista? Digite o nome a ser corrigido ("NÃO" ou "SAIR" ou "Q", para encerrar): ')

    #Verifica se o usuario informou um nome ou se deseja sair do programa
    if NomeOrig.upper() == "NÃO" or NomeOrig.upper() == "SAIR" or NomeOrig.upper() == "Q":
       break
    else:
        novoNome = input('Informe o novo nome: ') 

    #Verifica se o mesmo nome se repete na lista, e questiona qual o nome correto para ser corrigido
    if listaNomes.count(NomeOrig) > 1:
       indiceAlt = int(input(f'Existe mais de um {NomeOrig} na lista! Informe o numero do qual você quer alterar: ')) - 1
    else:
       indiceAlt = listaNomes.index(NomeOrig)

    #Corrige o nome na lista
    if indiceAlt >= 0 and indiceAlt <= len(listaNomes):
        listaNomes[indiceAlt] = novoNome       
    else:
        break    

    #Volta a imprimir a lista, para reiniciar o processo.
    os.system('cls')
    print('Aqui está sua lista (corrigida):')
    indiceNomes = 0
    for nome in listaNomes: 
        indiceNomes += 1
        print(f'{indiceNomes:02} : {nome}')

    print('\n')
