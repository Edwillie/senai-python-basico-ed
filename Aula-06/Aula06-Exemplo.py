MyGroup = {
    'Arroz':5.37,
    'Feijão':4.83,
    'Açúcar': 6.76
    }

valor_busca = 'Açúcar'

if valor_busca in MyGroup.keys():
    print(f'encontrado com o valor {MyGroup[valor_busca]}')
else:
    print(f'Desculpa, não encontrei {valor_busca} no dicionário')

# iterando entre os elementos do meu dicionário
for minha_chave, meu_valor in MyGroup.items():
    print(f'{minha_chave} = {meu_valor}')