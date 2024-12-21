#Mensagem Simples
print('passei aqui')

#Quebra de linha
print('Primeira mensagem\nSegunda mensagem')

#Usando caracter de escape \"
print("Que coisa mais \"linda\"") #Quando os caracteres de abertura e encerramento do texto precisam ser os mesmos
print('It\'s now or never') #Quando os caracteres de abertura e encerramento do texto precisam ser os mesmos

#Alternando forma de abertura e encerramento de textos, não é necessario o tratamento de escape
print("It's about what we did")
print('Agora a vaca foi pro "brejo"')

#Concatenadores
print("O Py "+'tá on',"e a virgula coloca um espacinho."+"Mas o mais, deixa tudo juntinho")

#Operadores nas mensagens
print("25 + 25") #somente emite conforme está entre aspas
print(25 + 25) #apresenta somente o resultado do calculo

#sep - Identificador de separador em substituição ao concatenador
print("colocando","traco","onde","coloquei","virgulas", sep="-")

#end - Coloca instrução adicional ao final da frase
print("curso de python",end=" é muito bacana!")
print("Nova mensagem") #Não quebra a linha por conta do end do comando anterior

#end - fica tudo na mesma linha
print("Comecei aqui", end=" ")
print("Terminei aqui") 
