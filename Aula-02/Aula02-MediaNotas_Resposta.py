passou = input('Será que você merece presente de natal?\nVocê Passou de ano?\n(Sim / Não): ')
nota1 = float(input('Qual foi sua 1a nota?\n'))
nota2 = float(input('Qual foi sua 2a nota?\n'))
nota3 = float(input('Qual foi sua 3a nota?\n'))
nota4 = float(input('Qual foi sua 4a nota?\n'))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Sua média foi {round(media,2)}!!!') 

if (media < 6) and passou.upper() == 'NÃO':
    print('Vamos pensar no caso! Reprovou nas notas, mas foi sicero!')
elif (media < 6) and passou.upper() == 'SIM':
    print('Mentiroso! Você não merece o presente!') 
elif (media >= 6) and passou.upper() == 'NÃO':
    print('Modesto! Você merece o presente! Porque passou de ano')
else:
    print('Parabéns. Você merece o presente!')
           