#Usando variaveis
nome = "Pedro"
print(nome) #Imprime o conteúdo da variavei

#A tipagem da variavel é de acordo com o valor atribuido
nome = "João"
idade = 25
idade = "vinte e cinco" #substituiu o numero por texto
print(idade)

#Multiplas atribuições
nome1, nome2 = "João", "Pedro"
print(nome1, nome2)

#Combinando textos com variaveis
print("Olá", nome1 + ". \nSeu colega", nome2,"disse que você tem", idade,"anos")

#Solicitando dados ao usuario
seuNome = input("Qual seu nome: ")
suaIdade = input("Qual sua idade: ")
seuPratoFavorito = input(f"{seuNome}, Me diz qual seu prato favorito? ")

print("Agora aprendi que o prato favorito do {seuNome} é: {seuPratoFavorito}")

