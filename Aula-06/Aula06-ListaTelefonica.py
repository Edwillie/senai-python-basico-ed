#Importando as bibliotecas para este programa
import os
import time

#Declarando a variavel global para o dicionário
ldic_listatel = {}

#Declaração de funções específicas desse programa
#Função para listar as opções
def menuOpcoes():
    print('***** BEM VINDO A AGENDA DE TELEFONE! *****')
    print('\nOPÇÕES:')
    print('1- Inserir um contato')
    print('2- Exibir a lista de contatos')
    print('3- Sair\n')
    lopcao = input('Digite sua opção: ')

    return lopcao

#Função para inserir um contato
def newFoneContact():
    os.system('cls')    
    print('***** CADASTRO DE NOVO CONTATO *****')
    lNome = input('Digite o nome do Contato: ')
    lTelefone = input('Digite o telefone do Contato: ')

    ldic_listatel[lNome] = lTelefone

    print('\nContato Registrado.')

#Função para listar os contatos existentes no dicionário
def listFoneContacts():
    os.system('cls')    
    print('***** AGENDA ATUALIZADA *****')

    for lnome, ltel in ldic_listatel.items():
        print(f'{lnome.upper()} : {ltel}')


#Iniciando o programa
while True:
    os.system('cls')    
    popcao = menuOpcoes()

    if popcao == '1':
        newFoneContact()
    elif popcao == '2':
        pass
    elif popcao == '3':
        break
    else:
        os.system('cls')
        print('Opção Inválida! Selecione uma das opções disponíveis')
        time.sleep(5)

