#Bibliotecas
import os

#Variaveis
listaNomes = []
listaIndices = []
indiceNomes = 0

while True:
    os.system('cls')
    nome = input('Insira um nome de uma pessoa: (ou pressione "Q", caso queira parar de inserir nomes) ')

    if nome.upper() == "Q":
        break
    else:
        indiceNomes += 1
        listaIndices.append(indiceNomes)
        listaNomes.append(nome)

print('Aqui está sua lista')
print(listaIndices, listaNomes)