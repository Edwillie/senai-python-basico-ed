# Aula 06

## Dicionários (Continuação)
Como visto anteriormente, um elemento do dicionário é composto por:
* Chave (Key)
* Valor (Value)

Um dicionário pode armazenar varios elementos. Assim como em uma lista, sendo conhecido como item.

Sendo, contudo, mais simples de operar do que uma lista. Pois pode ser acessado diretamente por sua chave:

```python
MyGroup = {
    'Arroz':5.37,
    'Feijão':4.83,
    'Açúcar': 6.76
    }

print(MyGroup['Feijão']) --Imprime na tela o valor 4,83 referente ao valor do item Feijão.    
```

### Trabalhando com dicionários
use o operador "_*in*_" para atuar sobre os elementos:
* key
* value
* items

Exemplo:
```python
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

```



